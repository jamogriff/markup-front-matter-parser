import re
from abc import ABC, abstractmethod
from ..invalid_front_matter_error import InvalidFrontMatterError
from ..markup_file import MarkupFile
from ..markup_content import MarkupContent
from ..file_format import FileFormat

class AbstractFrontMatterParser(ABC):
    """Provides shared parsing functionality for file-specific parsers.

    Subclasses need to implement the _parse_content() method and file_format
    and file_path properties. Subclasses are only meant to have one public method: parse().
    """

    @property
    @abstractmethod
    def file_path(self) -> str:
        raise NotImplementedError('Subclasses must implement this property')

    @property
    @abstractmethod
    def file_format(self) -> FileFormat:
        raise NotImplementedError('Subclasses must implement this property')

    @abstractmethod
    def _parse_content(self, file_lines: list[str], content_start_index: int) -> MarkupFile | None:
        raise NotImplementedError('Subclasses must implement this method')

    def parse(self) -> MarkupFile:
        """Parses a markdown (.md) file with simple (no multi-line) front matter.

        For example, parsing the file crazy_train.md:
        ---
        name: Crazy Train
        artist: Ozzy Osbourne
        ---
        # This is content.
        Hooray for content

        Would result in a MarkupFile object composed of:
        - A front_matter property: {'name': 'Crazy Train', 'artist': 'Ozzy Osbourne'}
        - TODO: update A content property: "# This is content.\nHooray for content\n"
        - A path property: crazy_train.md

        Raises:
            InvalidFrontMatterError: If front matter cannot be parsed (message will explain exact cause).
        """

        file_lines = self._extract_file_lines()
        front_matter = self._parse_front_matter(file_lines)
        content = self._parse_content(file_lines, self._get_content_start_index(front_matter))

        return MarkupFile(self.file_path, front_matter, content, self.file_format)

    def _extract_file_lines(self) -> list[str]:
        """Get an array of file lines from provided file path and validate initial structure.

        Note that this operation will pop off the first line of the file (the opening front matter tag).

        Raises:
            InvalidFrontMatterError:
                If file is empty.
                If file starts with anything other than opening front matter tag.
        """
        with open(self.file_path, "r") as file:
            file_lines = file.readlines()

        if len(file_lines) == 0:
            raise InvalidFrontMatterError("Encountered empty file")

        first_line = file_lines.pop(0)
        match = re.search("---", first_line)
        if not match:
            raise InvalidFrontMatterError(f"Expected front matter opening tag '---' at start of file, found: {first_line!r}")

        return file_lines

    def _parse_front_matter(self, file_lines: list[str]) -> dict[str, str]:
        """Parse front matter into a dict. Should be called prior to parsing content.
        
        Raises:
            InvalidFrontMatterError: If any line in between tags is not in the form "key: value"
        """
        front_matter = {}
        for line_index, line in enumerate(file_lines):
            front_matter_end = re.search("---", line)

            if front_matter_end:
                break

            key_pair = re.split(": ", line)

            if len(key_pair) != 2:
                raise InvalidFrontMatterError(f"Unable to parse key pair on line {line_index + 1}: {line!r}")

            front_matter[key_pair[0]] = key_pair[1].rstrip("\n")

        return front_matter

    def _get_content_start_index(self, front_matter: dict[str, str]) -> int:
        """Get the file line array index that body content starts at.

        We can deduce that the line for the file's content starts at index
        of number of properties + 1 (for the '---' tag).

        Note that we pop the first '---' tag off when asserting file
        starts with front matter, otherwise it would be + 2.
        """
        return len(front_matter.keys()) + 1
        
