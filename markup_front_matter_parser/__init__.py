"""See README.md for full details. Abbreviated usage is shown below:

from markup_front_matter_parser import FrontMatterParserFactory, MarkupFile, InvalidFrontMatterError
parser_factory = FrontMatterParserFactory()
parser = parser_factory.get_parser("songs/crazy-train.md")

try:
    markup_file: MarkupFile = parser.parse()
except InvalidFrontMatterException as e:
    [...]
"""
from .front_matter_parser_factory import FrontMatterParserFactory
from .models.markup_file import MarkupFile
from .models.markup_content import MarkupContent
from .invalid_front_matter_error import InvalidFrontMatterError
from .file_format import FileFormat

__version__ = "0.6.0"
__all__ = ("FrontMatterParserFactory", "MarkupFile", "MarkupContent", "FileFormat", "InvalidFrontMatterError")
