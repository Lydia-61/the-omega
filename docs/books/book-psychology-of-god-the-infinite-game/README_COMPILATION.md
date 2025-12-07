# LaTeX 编译说明 / LaTeX Compilation Instructions

## 中文版本 (Chinese Version)

使用 XeLaTeX 编译中文版本：

```bash
xelatex book-psychology-of-god-chinese.tex
xelatex book-psychology-of-god-chinese.tex  # 第二次编译以生成目录
```

或者使用 `latexmk`：

```bash
latexmk -xelatex book-psychology-of-god-chinese.tex
```

## 英文版本 (English Version)

使用 pdfLaTeX 或 XeLaTeX 编译英文版本：

```bash
pdflatex book-psychology-of-god-english.tex
pdflatex book-psychology-of-god-english.tex  # 第二次编译以生成目录
```

或者使用 `latexmk`：

```bash
latexmk -pdf book-psychology-of-god-english.tex
```

## 依赖项 (Dependencies)

### 中文版本需要的包：
- `ctex` (CTeX 宏包，用于中文支持)
- `amsmath`, `amssymb`, `amsthm` (数学公式)
- `graphicx` (图片)
- `hyperref` (超链接)
- `geometry` (页面布局)
- `enumitem` (列表)
- `microtype` (微调排版)

### 英文版本需要的包：
- `babel` (语言支持)
- 其他包与中文版本相同

## 注意事项 (Notes)

1. 确保 `architecture.png` 文件存在于同一目录下
2. 所有章节的 `.tex` 文件都已通过 `convert_md_to_tex.py` 从 Markdown 转换生成
3. 如果编译时出现错误，可能需要多次编译以正确生成交叉引用和目录
4. 中文版本必须使用 XeLaTeX 编译，因为需要中文字体支持

## 文件结构 (File Structure)

```
book-psychology-of-god-the-infinite-game/
├── book-psychology-of-god-chinese.tex    # 中文主文档
├── book-psychology-of-god-english.tex    # 英文主文档
├── foreword.tex                          # 中文序言
├── foreword_en.tex                       # 英文序言
├── interlude01-monologue-of-photon.tex    # 中文间奏 I
├── interlude01-monologue-of-photon_en.tex # 英文间奏 I
├── interlude02-last-atheist.tex          # 中文间奏 II
├── interlude02-last-atheist_en.tex       # 英文间奏 II
├── epilogue.tex                          # 中文结语
├── epilogue_en.tex                       # 英文结语
├── appendix-glossary.tex                  # 中文术语表
├── appendix-glossary_en.tex              # 英文术语表
├── appendix-bibliography.tex            # 中文参考文献
├── appendix-bibliography_en.tex         # 英文参考文献
├── architecture.png                      # 架构图
├── part01-geometry-of-void/             # 第一卷
├── part02-physics-of-passion/           # 第二卷
├── part03-engineering-of-awakening/      # 第三卷
├── part04-ethics-of-restraint/           # 第四卷
├── part05-topology-of-infinity/         # 第五卷
└── appendix-sacred-geometry-and-dynamics/ # 附录 A
```

