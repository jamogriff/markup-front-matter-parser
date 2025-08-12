import os
from .parsers.abstract_front_matter_parser import AbstractFrontMatterParser
from .parsers.markdown_front_matter_parser import MarkdownFrontMatterParser
from .parsers.html_front_matter_parser import HTMLFrontMatterParser

class FrontMatterParserFactory:

    def get_parser(self, file_path: str) -> AbstractFrontMatterParser:
        self._assert_is_file(file_path)
        ext = self._get_extension(file_path)

        if ext == '.md':
            return MarkdownFrontMatterParser(file_path)
        elif ext == '.html':
            return HTMLFrontMatterParser(file_path)
        else:
            raise ValueError(f"Unsupported file extension: {ext}")

    def _assert_is_file(self, file_path: str) -> None:
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

    def _get_extension(self, file_path: str) -> str:
        return os.path.splitext(file_path)[1].lower()

