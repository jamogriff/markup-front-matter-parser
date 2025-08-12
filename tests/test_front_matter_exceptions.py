import unittest
from pathlib import Path
from md_front_matter_parser.front_matter_parser_factory import FrontMatterParserFactory
from md_front_matter_parser.invalid_front_matter_error import InvalidFrontMatterError

class TestFrontMatterExceptions(unittest.TestCase):
    def setUp(self):
        self.parser_factory = FrontMatterParserFactory()
        self.fixtures_dir = Path(__file__).parent / "fixtures"

    def test_raises_exception_for_malformed_front_matter(self):
        file_path = self.fixtures_dir / 'malformed_front_matter.md'
        parser = self.parser_factory.get_parser(file_path)

        self.assertRaises(InvalidFrontMatterError, parser.parse)

    # TODO: move to factory tests, since error is thrown when creating the parser
    def test_raises_exception_for_non_markup_files(self):
        file_path = self.fixtures_dir / 'text_file.txt'
        parser = self.parser_factory.get_parser(file_path)

        self.assertRaises(ValueError, parser.parse)

    def test_raises_exception_for_empty_file(self):
        file_path = self.fixtures_dir / 'empty_file.md'
        parser = self.parser_factory.get_parser(file_path)

        self.assertRaises(InvalidFrontMatterError, parser.parse)

    def test_raises_exception_for_multiline_front_matter_property(self):
        file_path = self.fixtures_dir / 'front_matter_with_array.md'
        parser = self.parser_factory.get_parser(file_path)

        self.assertRaises(InvalidFrontMatterError, parser.parse)


