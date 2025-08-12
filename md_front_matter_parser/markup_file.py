from dataclasses import dataclass
from .file_format import FileFormat
from .markup_content import MarkupContent


@dataclass
class MarkupFile:
    """Represents a markup file with front matter,
    a file path reference, content and file format."""

    path: str
    front_matter: dict[str, str]
    content: MarkupContent | None
    file_format: FileFormat
