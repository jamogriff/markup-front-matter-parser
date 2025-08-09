import re
from songlist.markdown.markdown_file import MarkdownFile
from songlist.markdown.invalid_markdown_exception import InvalidMarkdownException

class MarkdownParser:
    """Parses a markdown (.md) file with simple (no multi-line) front matter. For example:
    ---
    name: Crazy Train
    artist: Ozzy Osbourne
    ---
    # This is content. Hooray for content

    Would be parsed into a Markdown object with a front_matter property
    a body property with a reference back to the file path.
    """

    def parse(self, file_path: str) -> MarkdownFile:
        with open(file_path, "r") as file:
            self._assert_markdown_file(file.name)
            file_lines = file.readlines()

        if len(file_lines) == 0:
            raise InvalidMarkdownException(file_path, 'Empty file encountered')

        match = re.search("---", file_lines.pop(0))
        if not match:
            raise InvalidMarkdownException(file_path, 'Malformed front matter encountered')

        front_matter = self._parse_front_matter(file_lines)

        # We can deduce that the line for the file's
        # body starts at index of (number of properties + 1 '---')
        # Note that we popped the first '---' off
        body_start_index = len(front_matter.keys()) + 1
        body = self._parse_body(file_lines, body_start_index)

        return MarkdownFile(file_path, front_matter, body)

    def _parse_front_matter(self, file_lines: list) -> dict:
        front_matter = {}
        for line in file_lines:
            front_matter_end = re.search("---", line)

            if front_matter_end:
                break

            match = re.split(": ", line)
            front_matter[match[0]] = match[1].rstrip("\n")

        return front_matter

    def _parse_body(self, file_lines: list, body_start_index: int) -> str:
        body_lines = file_lines[body_start_index:]

        body = ''
        for line in body_lines:
            body += line

        return body

    def _assert_markdown_file(self, file_name) -> str:
        """Asserts provided file name has an .md extension"""
        match = re.search(r'\.(.+)', file_name)

        if not match:
            raise InvalidMarkdownException(file_name, "Missing file extension")

        assert match.group() == ".md"

