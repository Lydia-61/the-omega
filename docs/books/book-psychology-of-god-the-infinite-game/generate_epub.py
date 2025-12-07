#!/usr/bin/env python3
"""
Generate EPUB eBooks from Markdown files.
"""

import os
from pathlib import Path

def create_master_markdown(language='chinese'):
    """Create a master Markdown file combining all chapters."""
    base_dir = Path(__file__).parent
    
    # Determine file suffix
    suffix = '_en' if language == 'english' else ''
    
    # File order based on book structure
    if language == 'chinese':
        files = [
            'foreword.md',
            'part01-geometry-of-void/chapter01-prison-of-omniscience/01-01-paralysis-of-the-almighty.md',
            'part01-geometry-of-void/chapter01-prison-of-omniscience/01-02-weight-of-the-void.md',
            'part01-geometry-of-void/chapter02-big-bang-as-dissociation/02-01-first-distinction.md',
            'part01-geometry-of-void/chapter02-big-bang-as-dissociation/02-02-mechanism-of-kenosis.md',
            'interlude01-monologue-of-photon.md',
            'part02-physics-of-passion/chapter03-golden-straitjacket/03-01-light-speed-delay-of-thought.md',
            'part02-physics-of-passion/chapter03-golden-straitjacket/03-02-gravity-geometrization-of-love.md',
            'part02-physics-of-passion/chapter03-golden-straitjacket/03-03-planck-constant-art-of-resolution.md',
            'part02-physics-of-passion/chapter04-error-function-of-pain/04-01-negative-feedback-mechanism.md',
            'part02-physics-of-passion/chapter04-error-function-of-pain/04-02-topology-of-evil.md',
            'part02-physics-of-passion/chapter05-death-as-iteration/05-01-ship-of-theseus.md',
            'part02-physics-of-passion/chapter05-death-as-iteration/05-02-relay-of-genes-and-memes.md',
            'interlude02-last-atheist.md',
            'part03-engineering-of-awakening/chapter06-mutiny-of-observer/06-01-copernican-inversion.md',
            'part03-engineering-of-awakening/chapter06-mutiny-of-observer/06-02-technology-as-theology.md',
            'part03-engineering-of-awakening/chapter07-lucid-dreaming/07-01-vacuum-engineering.md',
            'part03-engineering-of-awakening/chapter07-lucid-dreaming/07-02-maxwell-demon-anti-entropy.md',
            'part04-ethics-of-restraint/chapter08-temptation-of-cheat-codes/08-01-perfect-nothingness.md',
            'part04-ethics-of-restraint/chapter08-temptation-of-cheat-codes/08-02-edge-of-logical-collapse.md',
            'part04-ethics-of-restraint/chapter09-great-refusal/09-01-covenant.md',
            'part04-ethics-of-restraint/chapter09-great-refusal/09-02-inevitability-of-aesthetics.md',
            'part05-topology-of-infinity/chapter10-refutation-of-heat-death/10-01-trinitarian-equivalence.md',
            'part05-topology-of-infinity/chapter10-refutation-of-heat-death/10-02-escape-velocity-of-meaning.md',
            'part05-topology-of-infinity/chapter11-life-of-n-plus-one/11-01-spiral-time.md',
            'part05-topology-of-infinity/chapter11-life-of-n-plus-one/11-02-open-ended-finale.md',
            'epilogue.md',
            'appendix-sacred-geometry-and-dynamics/A-01-dynamics-of-will.md',
            'appendix-sacred-geometry-and-dynamics/A-02-thermodynamic-basis-of-ethics.md',
            'appendix-sacred-geometry-and-dynamics/A-03-roadmap-of-ultimate-civilizations.md',
            'appendix-glossary.md',
            'appendix-bibliography.md',
        ]
    else:  # english
        files = [
            'foreword_en.md',
            'part01-geometry-of-void/chapter01-prison-of-omniscience/01-01-paralysis-of-the-almighty_en.md',
            'part01-geometry-of-void/chapter01-prison-of-omniscience/01-02-weight-of-the-void_en.md',
            'part01-geometry-of-void/chapter02-big-bang-as-dissociation/02-01-first-distinction_en.md',
            'part01-geometry-of-void/chapter02-big-bang-as-dissociation/02-02-mechanism-of-kenosis_en.md',
            'interlude01-monologue-of-photon_en.md',
            'part02-physics-of-passion/chapter03-golden-straitjacket/03-01-light-speed-delay-of-thought_en.md',
            'part02-physics-of-passion/chapter03-golden-straitjacket/03-02-gravity-geometrization-of-love_en.md',
            'part02-physics-of-passion/chapter03-golden-straitjacket/03-03-planck-constant-art-of-resolution_en.md',
            'part02-physics-of-passion/chapter04-error-function-of-pain/04-01-negative-feedback-mechanism_en.md',
            'part02-physics-of-passion/chapter04-error-function-of-pain/04-02-topology-of-evil_en.md',
            'part02-physics-of-passion/chapter05-death-as-iteration/05-01-ship-of-theseus_en.md',
            'part02-physics-of-passion/chapter05-death-as-iteration/05-02-relay-of-genes-and-memes_en.md',
            'interlude02-last-atheist_en.md',
            'part03-engineering-of-awakening/chapter06-mutiny-of-observer/06-01-copernican-inversion_en.md',
            'part03-engineering-of-awakening/chapter06-mutiny-of-observer/06-02-technology-as-theology_en.md',
            'part03-engineering-of-awakening/chapter07-lucid-dreaming/07-01-vacuum-engineering_en.md',
            'part03-engineering-of-awakening/chapter07-lucid-dreaming/07-02-maxwell-demon-anti-entropy_en.md',
            'part04-ethics-of-restraint/chapter08-temptation-of-cheat-codes/08-01-perfect-nothingness_en.md',
            'part04-ethics-of-restraint/chapter08-temptation-of-cheat-codes/08-02-edge-of-logical-collapse_en.md',
            'part04-ethics-of-restraint/chapter09-great-refusal/09-01-covenant_en.md',
            'part04-ethics-of-restraint/chapter09-great-refusal/09-02-inevitability-of-aesthetics_en.md',
            'part05-topology-of-infinity/chapter10-refutation-of-heat-death/10-01-trinitarian-equivalence_en.md',
            'part05-topology-of-infinity/chapter10-refutation-of-heat-death/10-02-escape-velocity-of-meaning_en.md',
            'part05-topology-of-infinity/chapter11-life-of-n-plus-one/11-01-spiral-time_en.md',
            'part05-topology-of-infinity/chapter11-life-of-n-plus-one/11-02-open-ended-finale_en.md',
            'epilogue_en.md',
            'appendix-sacred-geometry-and-dynamics/A-01-dynamics-of-will_en.md',
            'appendix-sacred-geometry-and-dynamics/A-02-thermodynamic-basis-of-ethics_en.md',
            'appendix-sacred-geometry-and-dynamics/A-03-roadmap-of-ultimate-civilizations_en.md',
            'appendix-glossary_en.md',
            'appendix-bibliography_en.md',
        ]
    
    # Create master markdown content
    master_content = []
    
    # Add title
    if language == 'chinese':
        master_content.append('# 上帝的心理学：无限的游戏\n\n')
        master_content.append('**The Psychology of God: The Infinite Game**\n\n')
        master_content.append('本书是系列丛书的第五部，探讨宇宙心智的深层结构、神性的心理学基础以及存在的终极意义。\n\n')
    else:
        master_content.append('# The Psychology of God: The Infinite Game\n\n')
        master_content.append('**上帝的心理学：无限的游戏**\n\n')
        master_content.append('This is the fifth volume of the series, exploring the deep structure of the cosmic mind, the psychological foundations of divinity, and the ultimate meaning of existence.\n\n')
    
    # Add architecture image
    master_content.append('![Architecture Diagram](architecture.png)\n\n')
    master_content.append('---\n\n')
    
    # Combine all files
    for file_path in files:
        full_path = base_dir / file_path
        if full_path.exists():
            print(f"Adding: {file_path}")
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
                # Add page break before each chapter
                master_content.append('\n\n---\n\n')
                master_content.append(content)
                master_content.append('\n\n')
        else:
            print(f"Warning: File not found: {file_path}")
    
    # Write master file
    output_file = base_dir / f'book-master-{language}.md'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(''.join(master_content))
    
    print(f"\nCreated master Markdown file: {output_file}")
    return output_file

def create_epub_metadata(language='chinese'):
    """Create EPUB metadata file."""
    base_dir = Path(__file__).parent
    
    if language == 'chinese':
        metadata = {
            'title': '上帝的心理学：无限的游戏',
            'title_en': 'The Psychology of God: The Infinite Game',
            'author': 'Haobo Ma',
            'language': 'zh-CN',
            'date': '2025',
            'description': '本书是系列丛书的第五部，探讨宇宙心智的深层结构、神性的心理学基础以及存在的终极意义。',
        }
    else:
        metadata = {
            'title': 'The Psychology of God: The Infinite Game',
            'title_zh': '上帝的心理学：无限的游戏',
            'author': 'Haobo Ma',
            'language': 'en-US',
            'date': '2025',
            'description': 'This is the fifth volume of the series, exploring the deep structure of the cosmic mind, the psychological foundations of divinity, and the ultimate meaning of existence.',
        }
    
    # Create metadata file in YAML format
    metadata_file = base_dir / f'epub-metadata-{language}.yaml'
    with open(metadata_file, 'w', encoding='utf-8') as f:
        f.write('---\n')
        f.write(f'title: "{metadata["title"]}"\n')
        f.write(f'author: "{metadata["author"]}"\n')
        f.write(f'language: {metadata["language"]}\n')
        f.write(f'date: {metadata["date"]}\n')
        f.write(f'description: "{metadata["description"]}"\n')
        f.write('---\n')
    
    print(f"Created metadata file: {metadata_file}")
    return metadata_file

def generate_epub(language='chinese'):
    """Generate EPUB file using pandoc."""
    import subprocess
    
    base_dir = Path(__file__).parent
    
    # Create master markdown
    master_md = create_master_markdown(language)
    
    # Create metadata
    metadata_file = create_epub_metadata(language)
    
    # Output EPUB file
    output_epub = base_dir / f'book-psychology-of-god-{language}.epub'
    
    # Build pandoc command
    cmd = [
        'pandoc',
        str(master_md),
        '--metadata-file', str(metadata_file),
        '--epub-cover-image', str(base_dir / 'architecture.png'),
        '--toc',
        '--toc-depth', '3',
        '--mathml',
        '--standalone',
        '-o', str(output_epub)
    ]
    
    print(f"\nGenerating EPUB: {output_epub}")
    print(f"Command: {' '.join(cmd)}\n")
    
    # Run pandoc
    result = subprocess.run(cmd, cwd=str(base_dir), capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"✓ Successfully generated: {output_epub}")
        # Check file size
        size = output_epub.stat().st_size / (1024 * 1024)  # MB
        print(f"  File size: {size:.2f} MB")
    else:
        print(f"✗ Error generating EPUB:")
        print(result.stderr)
        return False
    
    return True

def main():
    """Main function."""
    print("=" * 60)
    print("EPUB Generation Script")
    print("=" * 60)
    
    # Generate Chinese EPUB
    print("\n[1/2] Generating Chinese EPUB...")
    generate_epub('chinese')
    
    # Generate English EPUB
    print("\n[2/2] Generating English EPUB...")
    generate_epub('english')
    
    print("\n" + "=" * 60)
    print("EPUB generation complete!")
    print("=" * 60)

if __name__ == '__main__':
    main()

