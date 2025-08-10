class AbstractFrontMatterParser:
    """Provides shared parsing functionality for file-specific parsers."""

    def _parse_front_matter(self, file_lines: list[str]) -> dict[str, str]:
        front_matter = {}
        for line_index, line in enumerate(file_lines):
            front_matter_end = re.search("---", line)

            if front_matter_end:
                break

            key_pair = re.split(": ", line)

            if len(key_pair) != 2:
                raise ValueError(f"Unable to parse key pair on line {line_index + 1}")

            front_matter[key_pair[0]] = key_pair[1].rstrip("\n")

        return front_matter

    def _parse_body(self, file_lines: list[str], body_start_index: int):
        raise NotImplementedError('Subclasses must implement their own take on this method')
