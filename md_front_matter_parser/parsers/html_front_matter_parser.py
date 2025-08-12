from .abstract_front_matter_parser import AbstractFrontMatterParser
from ..file_format import FileFormat
from ..markup_content import MarkupContent

class HTMLFrontMatterParser(AbstractFrontMatterParser):

    def __init__(self, file_path: str):
        self._file_path = file_path

    @property
    def file_path(self) -> str:
        return self._file_path

    @property
    def file_format(self) -> FileFormat:
        return FileFormat.HTML

    def _parse_content(self, file_lines: list[str], content_start_index: int) -> MarkupContent | None:
        content_lines = file_lines[content_start_index:]

        content = ""
        for line in content_lines:
            content += line

        if content == "":
            return None
        else:
            return MarkupContent(content)
