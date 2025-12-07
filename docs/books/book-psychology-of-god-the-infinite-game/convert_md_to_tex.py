#!/usr/bin/env python3
"""
Convert Markdown files to LaTeX format for book compilation.
"""

import re
import os
from pathlib import Path

def escape_latex_simple(text, escape_braces=True):
    """Escape special LaTeX characters (assumes math and LaTeX commands are already protected)."""
    special_chars = {
        '&': r'\&',
        '%': r'\%',
        '#': r'\#',
        '^': r'\textasciicircum{}',
        '_': r'\_',
        '~': r'\textasciitilde{}',
    }
    
    if escape_braces:
        special_chars['{'] = r'\{'
        special_chars['}'] = r'\}'
    
    result = text
    for char, replacement in special_chars.items():
        result = result.replace(char, replacement)
    
    return result

def escape_latex(text):
    """Escape special LaTeX characters, but preserve math expressions."""
    # First, protect math expressions
    math_placeholders = []
    math_counter = 0
    
    def protect_math(match):
        nonlocal math_counter
        placeholder = f'__MATH_{math_counter}__'
        math_placeholders.append((placeholder, match.group(0)))
        math_counter += 1
        return placeholder
    
    # Protect inline math $...$
    text = re.sub(r'\$([^$\n]+?)\$', protect_math, text)
    
    # Escape special characters
    text = escape_latex_simple(text)
    
    # Restore math expressions
    for placeholder, original in math_placeholders:
        text = text.replace(placeholder, original)
    
    return text

def convert_markdown_to_latex(md_content):
    """Convert markdown content to LaTeX format."""
    lines = md_content.split('\n')
    latex_lines = []
    in_math_block = False
    in_list = False
    in_blockquote = False
    
    i = 0
    while i < len(lines):
        line = lines[i]
        original_line = line
        
        # Check if we're entering/exiting math block
        if '$$' in line:
            if not in_math_block:
                # Opening math block
                in_math_block = True
                # Replace $$ with \[
                line = line.replace('$$', '\\[', 1)
                if '$$' in line:
                    # Single line math block
                    line = line.replace('$$', '\\]')
                    in_math_block = False
            else:
                # Closing math block
                in_math_block = True
                line = line.replace('$$', '\\]', 1)
                in_math_block = False
        
        # If we're in a math block, keep as is (but handle $$ markers)
        if in_math_block:
            if '$$' in line:
                line = line.replace('$$', '\\]')
                in_math_block = False
            latex_lines.append(line)
            i += 1
            continue
        
        # Handle blockquotes
        if line.strip().startswith('>'):
            if not in_blockquote:
                latex_lines.append('\\begin{quote}')
                in_blockquote = True
            # Remove > and process the rest
            quote_text = line.lstrip('> ').strip()
            # Process markdown in quote
            quote_text = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', quote_text)
            quote_text = re.sub(r'\*(.+?)\*', r'\\textit{\1}', quote_text)
            # Escape LaTeX special chars (but preserve math)
            quote_text = escape_latex(quote_text)
            # Restore math expressions
            quote_text = re.sub(r'\\\$\\\$([^\\]+?)\\\$\\\$', r'$\1$', quote_text)
            quote_text = re.sub(r'\\\$([^\\]+?)\\\$', r'$\1$', quote_text)
            latex_lines.append(quote_text)
            # Check if next line is also a quote
            if i + 1 < len(lines) and not lines[i + 1].strip().startswith('>'):
                latex_lines.append('\\end{quote}')
                in_blockquote = False
            i += 1
            continue
        
        # Close blockquote if needed
        if in_blockquote and not line.strip().startswith('>'):
            latex_lines.append('\\end{quote}')
            in_blockquote = False
        
        # Handle horizontal rules
        if line.strip() == '---' or line.strip() == '***':
            latex_lines.append('\\bigskip')
            latex_lines.append('\\hrule')
            latex_lines.append('\\bigskip')
            i += 1
            continue
        
        # Handle headers
        if line.startswith('#'):
            # Count # to determine level
            level = len(line) - len(line.lstrip('#'))
            header_text = line.lstrip('#').strip()
            
            # Close list if needed
            if in_list:
                latex_lines.append('\\end{itemize}')
                in_list = False
            
            # Process header text (handle bold, math, etc.)
            header_text = process_inline_formatting(header_text)
            
            if level == 1:
                latex_lines.append(f'\\section{{{header_text}}}')
            elif level == 2:
                latex_lines.append(f'\\subsection{{{header_text}}}')
            elif level == 3:
                latex_lines.append(f'\\subsubsection{{{header_text}}}')
            elif level == 4:
                # Use paragraph or bold
                latex_lines.append(f'\\paragraph{{{header_text}}}')
            else:
                latex_lines.append(f'\\textbf{{{header_text}}}')
            i += 1
            continue
        
        # Handle lists
        if line.strip().startswith('-') or line.strip().startswith('*'):
            if not in_list:
                latex_lines.append('\\begin{itemize}')
                in_list = True
            
            # Extract list item text
            item_text = line.lstrip('-* ').strip()
            # Process formatting
            item_text = process_inline_formatting(item_text)
            latex_lines.append(f'\\item {item_text}')
            i += 1
            continue
        
        # Close list if needed
        if in_list and line.strip() == '':
            # Check if next non-empty line is also a list item
            j = i + 1
            while j < len(lines) and lines[j].strip() == '':
                j += 1
            if j >= len(lines) or (not lines[j].strip().startswith('-') and not lines[j].strip().startswith('*')):
                latex_lines.append('\\end{itemize}')
                in_list = False
        
        # Handle empty lines
        if line.strip() == '':
            latex_lines.append('')
            i += 1
            continue
        
        # Handle HTML tags
        if '<' in line and '>' in line:
            # Remove HTML tags
            line = re.sub(r'<[^>]+>', '', line)
            # Handle <br> as line break
            if '<br>' in original_line or '<br/>' in original_line:
                latex_lines.append('\\\\')
                i += 1
                continue
        
        # Regular paragraph text
        if line.strip():
            processed_line = process_inline_formatting(line)
            latex_lines.append(processed_line)
        
        i += 1
    
    # Close any open environments
    if in_list:
        latex_lines.append('\\end{itemize}')
    if in_blockquote:
        latex_lines.append('\\end{quote}')
    
    return '\n'.join(latex_lines)

def process_inline_formatting(text):
    """Process inline markdown formatting (bold, italic, math, etc.)."""
    # Step 1: Protect math expressions first
    math_placeholders = []
    math_counter = 0
    
    def protect_math(match):
        nonlocal math_counter
        placeholder = f'__MATH_{math_counter}__'
        math_placeholders.append((placeholder, match.group(0)))
        math_counter += 1
        return placeholder
    
    # Protect inline math $...$
    text = re.sub(r'\$([^$\n]+?)\$', protect_math, text)
    
    # Protect display math $$...$$ (shouldn't be here, but just in case)
    text = re.sub(r'\$\$([^$]+?)\$\$', protect_math, text)
    
    # Step 2: Convert markdown formatting to LaTeX commands
    # Process bold **text** - but protect content first
    def process_bold(match):
        content = match.group(1)
        # Escape content but preserve math placeholders
        parts = re.split(r'(__MATH_\d+__)', content)
        escaped_parts = []
        for part in parts:
            if part.startswith('__MATH_'):
                escaped_parts.append(part)
            else:
                escaped_parts.append(escape_latex_simple(part, escape_braces=False))
        escaped_content = ''.join(escaped_parts)
        return f'\\textbf{{{escaped_content}}}'
    
    text = re.sub(r'\*\*(.+?)\*\*', process_bold, text)
    
    # Process italic *text* (but not if it's part of **text**)
    def process_italic(match):
        content = match.group(1)
        parts = re.split(r'(__MATH_\d+__)', content)
        escaped_parts = []
        for part in parts:
            if part.startswith('__MATH_'):
                escaped_parts.append(part)
            else:
                escaped_parts.append(escape_latex_simple(part, escape_braces=False))
        escaped_content = ''.join(escaped_parts)
        return f'\\textit{{{escaped_content}}}'
    
    text = re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', process_italic, text)
    
    # Process code `text`
    def process_code(match):
        content = match.group(1)
        escaped_content = escape_latex_simple(content, escape_braces=False)
        return f'\\texttt{{{escaped_content}}}'
    
    text = re.sub(r'`([^`]+?)`', process_code, text)
    
    # Step 3: Protect LaTeX commands we just created
    # Use a simple approach: find \command{...} patterns and protect them
    latex_cmd_placeholders = []
    cmd_counter = [0]  # Use list to allow modification in nested function
    
    def protect_latex_cmd_inner(match):
        placeholder = f'__LATEX_CMD_{cmd_counter[0]}__'
        latex_cmd_placeholders.append((placeholder, match.group(0)))
        cmd_counter[0] += 1
        return placeholder
    
    # Protect LaTeX commands: \command{...} - match simple cases first
    # This is a simplified version that works for most cases
    # We'll do multiple passes to handle nested cases
    max_iterations = 10
    iteration = 0
    while iteration < max_iterations:
        old_text = text
        # Match \command{content} where content doesn't contain unmatched braces
        text = re.sub(r'\\([a-zA-Z]+)\{([^{}]*)\}', protect_latex_cmd_inner, text)
        if old_text == text:
            break
        iteration += 1
    
    # Step 4: Escape remaining special characters
    parts = re.split(r'(__MATH_\d+__|__LATEX_CMD_\d+__)', text)
    result_parts = []
    for part in parts:
        if part.startswith('__MATH_') or part.startswith('__LATEX_CMD_'):
            result_parts.append(part)
        else:
            result_parts.append(escape_latex_simple(part, escape_braces=True))
    text = ''.join(result_parts)
    
    # Step 5: Restore LaTeX commands
    for placeholder, original in latex_cmd_placeholders:
        text = text.replace(placeholder, original)
    
    # Step 6: Restore math expressions
    for placeholder, original in math_placeholders:
        text = text.replace(placeholder, original)
    
    return text

def convert_file(md_path, tex_path):
    """Convert a single markdown file to LaTeX."""
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    latex_content = convert_markdown_to_latex(md_content)
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(tex_path), exist_ok=True)
    
    with open(tex_path, 'w', encoding='utf-8') as f:
        f.write(latex_content)
    
    print(f"Converted: {md_path} -> {tex_path}")

def main():
    """Main conversion function."""
    base_dir = Path(__file__).parent
    
    # Find all .md files
    md_files = list(base_dir.rglob('*.md'))
    
    # Filter out index files (we'll handle them separately)
    md_files = [f for f in md_files if f.name != 'index.md' and f.name != 'index_en.md']
    
    for md_file in md_files:
        # Create corresponding .tex path
        tex_file = md_file.with_suffix('.tex')
        convert_file(md_file, tex_file)
    
    print(f"\nConverted {len(md_files)} files.")

if __name__ == '__main__':
    main()

