from dataclasses import dataclass

@dataclass
class MarkdownFile:
    """Represents contents of a markdown file with front matter."""
    path: str
    front_matter: dict
    body: str
