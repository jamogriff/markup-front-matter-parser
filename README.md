# Markdown Front Matter Parser

This is a simple Python package for parsing Markdown files with Front Matter. It was specifically designed to be used
on [Jekyll files](https://jekyllrb.com/docs/front-matter/), but will work on 
Although Jekyll's implementation of front matter is YAML, this package
_does not support_ parsing multi-line properties (e.g. YAML lists).

## Usage
`from md_front_matter_parser import MarkdownFrontMatterParser, InvalidMarkdownFile`
