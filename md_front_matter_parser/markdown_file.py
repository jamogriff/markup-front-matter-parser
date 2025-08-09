from dataclasses import dataclass

@dataclass
class MarkdownFile:
    """Represents contents of a markdown file with
    front matter and a reference back to the file path"""
    path: str
    front_matter: dict
    body: str
