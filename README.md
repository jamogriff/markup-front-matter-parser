# Markup Front Matter Parser

This is a Python package for parsing the Front Matter of markup files (e.g. .md, .html).
Front Matter is a `YAML` snippet at the top of a markup file that stores metadata
that is used commonly in [Jekyll](https://jekyllrb.com/docs/front-matter/) static sites.

Note that this package is a simple front matter parser that will only parse single
line key-values. It currently __does not support__ parsing multi-line front matter mapping entries (e.g. `YAML` lists).


## Usage

Install the package with:
```
pip install markup-front-matter-parser
```

In your code import the following:
```
from markup_front_matter_parser import FrontMatterParserFactory, InvalidFrontMatterError
```
**Note:** If you'd like to add type-hints to objects, then you can additionally import `MarkupFile`, `MarkupContent`, and `FileFormat`.

To use in your code, start by creating an instance of `FrontMatterParserFactory` and then call `get_parser()` with the desired file you want parsed:
```
parser_factory = FrontMatterParserFactory()
parser: AbstractFrontMatterParser = parser_factory.get_parser("songs/crazy-train.md")
```

Obtaining the parser may raise a `ValueError` if the file type is incompatible and a `FileNotFoundError` if the file is not found.
Calling `parse()` on this parser instance will return a `MarkupFile` instance that contains the parsed front matter and other attributes:
```
try:
    markup_file: MarkupFile = parser.parse()
except InvalidFrontMatterException as e:
    [...]
```

For example, parsing the file `crazy_train.md`:
```
---
name: Crazy Train
artist: Ozzy Osbourne
---
# This is content.
Hooray for content
```

Would result in a `MarkupFile` object composed of:
- A front_matter attribute: `{"name": "Crazy Train", "artist": "Ozzy Osbourne"}`
- A content attribute (an instance of `MarkupContent` [specifically the `raw` attribute]): `"# This is content.\nHooray for content\n"`
- A path attribute: `"crazy_train.md"`
- A file_format attribute: `FileFormat.MARKDOWN`

The `parse()` method will raise an informative `InvalidFrontMatterError` if the file's front matter cannot be parsed.


## Code Overview

This was written within the context of an in-depth sprint of learning Python, so it may not be the most practical package for the job.
The architecture of the package uses the factory pattern and was designed so that future improvements would not change the public API.
In addition, each subclass of `AbstractFrontMatterParser` could easily implement their own tokenizing of file-specific markup content.
In this fashion, the package could then become a holistic markup parser rather than solely just a front matter parser.


