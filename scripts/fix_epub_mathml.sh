#!/bin/bash

# EPUB MathML Property Fix Script
# Usage: ./fix_epub_mathml.sh <epub-file>
# Example: ./fix_epub_mathml.sh book.epub

set -e

EPUB_FILE="$1"

if [ -z "$EPUB_FILE" ]; then
    echo "Usage: $0 <epub-file>"
    exit 1
fi

# Convert to absolute path
if [ -f "$EPUB_FILE" ]; then
    EPUB_FILE_ABS=$(cd "$(dirname "$EPUB_FILE")" && pwd)/$(basename "$EPUB_FILE")
elif [ -f "$(pwd)/$EPUB_FILE" ]; then
    EPUB_FILE_ABS="$(pwd)/$EPUB_FILE"
else
    echo "Error: EPUB file not found: $EPUB_FILE"
    exit 1
fi

if [ ! -f "$EPUB_FILE_ABS" ]; then
    echo "Error: EPUB file not found: $EPUB_FILE_ABS"
    exit 1
fi
EPUB_DIR=$(dirname "$EPUB_FILE_ABS")
EPUB_NAME=$(basename "$EPUB_FILE_ABS" .epub)
TEMP_DIR="${EPUB_DIR}/epub_temp_$$"
BACKUP_FILE="${EPUB_FILE_ABS}.backup"

echo "Fixing MathML property in: $EPUB_FILE_ABS"

# Cleanup function
cleanup() {
    rm -rf "$TEMP_DIR" 2>/dev/null || true
}

# Set trap to cleanup on exit
trap cleanup EXIT INT TERM

# Create backup
echo "Step 1: Creating backup..."
cp "$EPUB_FILE_ABS" "$BACKUP_FILE" || {
    echo "Error: Failed to create backup"
    exit 1
}

# Extract EPUB
echo "Step 2: Extracting EPUB..."
unzip -q -o "$EPUB_FILE_ABS" -d "$TEMP_DIR" || {
    echo "Error: Failed to extract EPUB"
    exit 1
}

# Fix OPF file
OPF_FILE="$TEMP_DIR/EPUB/content.opf"
if [ ! -f "$OPF_FILE" ]; then
    echo "Error: OPF file not found in EPUB"
    exit 1
fi

# Find all XHTML files containing MathML
FILES_NEEDING_FIX=0
FIXED_COUNT=0

# Check nav.xhtml specifically (has special "nav" property)
NAV_FILE="$TEMP_DIR/EPUB/nav.xhtml"
if [ -f "$NAV_FILE" ] && grep -q "<math" "$NAV_FILE" 2>/dev/null; then
    if grep -q 'properties="nav"' "$OPF_FILE" && ! grep -q 'properties="nav mathml"' "$OPF_FILE"; then
        echo "Step 3: Adding mathml property to nav.xhtml..."
        sed -i '' 's/properties="nav"/properties="nav mathml"/g' "$OPF_FILE" 2>/dev/null || \
        sed -i 's/properties="nav"/properties="nav mathml"/g' "$OPF_FILE"
        echo "  ✓ Fixed nav.xhtml MathML property"
        FILES_NEEDING_FIX=1
        FIXED_COUNT=$((FIXED_COUNT + 1))
    fi
fi

# Check all other XHTML/HTML files
echo "Step 3: Checking all XHTML files for MathML..."
for xhtml_file in $(find "$TEMP_DIR/EPUB" -type f \( -name "*.xhtml" -o -name "*.html" \) ! -name "nav.xhtml"); do
    if grep -q "<math" "$xhtml_file" 2>/dev/null; then
        # Get the href path relative to EPUB root
        xhtml_rel_path=$(echo "$xhtml_file" | sed "s|^$TEMP_DIR/EPUB/||")
        xhtml_basename=$(basename "$xhtml_file")
        
        # Find the item in OPF manifest for this file
        # Match href that ends with the filename
        if grep -q "href=\"[^\"]*$xhtml_basename\"" "$OPF_FILE" 2>/dev/null; then
            # Check if mathml property is missing
            item_line=$(grep "href=\"[^\"]*$xhtml_basename\"" "$OPF_FILE" | head -1)
            if echo "$item_line" | grep -qv 'properties="[^"]*mathml'; then
                # Add mathml property
                if echo "$item_line" | grep -q 'properties="'; then
                    # Property already exists, add mathml to it
                    sed -i '' "s|\(href=\"[^\"]*$xhtml_basename\"[^>]*properties=\"\)\([^\"]*\)\"|\\1\\2 mathml\"|g" "$OPF_FILE" 2>/dev/null || \
                    sed -i "s|\(href=\"[^\"]*$xhtml_basename\"[^>]*properties=\"\)\([^\"]*\)\"|\\1\\2 mathml\"|g" "$OPF_FILE"
                else
                    # No properties attribute, add it
                    sed -i '' "s|\(href=\"[^\"]*$xhtml_basename\"[^>]*\)/>|\\1 properties=\"mathml\" />|g" "$OPF_FILE" 2>/dev/null || \
                    sed -i "s|\(href=\"[^\"]*$xhtml_basename\"[^>]*\)/>|\\1 properties=\"mathml\" />|g" "$OPF_FILE"
                fi
                echo "  ✓ Fixed $xhtml_basename MathML property"
                FILES_NEEDING_FIX=1
                FIXED_COUNT=$((FIXED_COUNT + 1))
            fi
        fi
    fi
done

if [ $FILES_NEEDING_FIX -eq 1 ]; then
    # Rebuild EPUB
    echo "Step 4: Repackaging EPUB..."
    rm -f "$EPUB_FILE_ABS"
    cd "$TEMP_DIR" || exit 1
    zip -0 -X "$EPUB_FILE_ABS" mimetype 2>/dev/null || {
        echo "Error: Failed to create EPUB"
        cd "$EPUB_DIR"
        mv "$BACKUP_FILE" "$EPUB_FILE_ABS"
        exit 1
    }
    zip -r "$EPUB_FILE_ABS" . -x mimetype "*.DS_Store" >/dev/null 2>&1
    cd "$EPUB_DIR"
    
    # Remove backup if successful
    rm -f "$BACKUP_FILE"
    echo ""
    echo "✓ EPUB fixed successfully: $EPUB_FILE_ABS ($FIXED_COUNT file(s) updated)"
else
    echo "Step 3: All MathML properties already present or no MathML found"
    rm -f "$BACKUP_FILE"
fi
