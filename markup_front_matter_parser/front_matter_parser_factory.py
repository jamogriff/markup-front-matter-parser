import os
from .file_format import FileFormat
from .parsers.abstract_front_matter_parser import AbstractFrontMatterParser
from .parsers.markdown_front_matter_parser import MarkdownFrontMatterParser
from .parsers.html_front_matter_parser import HTMLFrontMatterParser

class FrontMatterParserFactory:
    """Class for creating instances of FrontMatterParsers."""

    def get_parser(self, file_path: str) -> AbstractFrontMatterParser:
        """Return instance of subclass of AbstractFrontMatterParser dependent
        on the file desired to be parsed.

        Raises:
            ValueError: If file extension is not .md or .html.
            FileNoteFoundError: If file does not exist.
        """

        self._assert_is_file(file_path)
        ext = self._get_extension(file_path)

        if ext == FileFormat.MARKDOWN.value:
            return MarkdownFrontMatterParser(file_path)
        elif ext == FileFormat.HTML.value:
            return HTMLFrontMatterParser(file_path)
        else:
            raise ValueError(f"Unsupported file extension: {ext}")

    def _assert_is_file(self, file_path: str) -> None:
        """Assert the file is on the filesystem.

        Raises:
            FileNotFoundError: If file does not exist.
        """

        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

    def _get_extension(self, file_path: str) -> str:
        """Return file extension (e.g. .md, .html, .json)"""

        return os.path.splitext(file_path)[1].lower()

