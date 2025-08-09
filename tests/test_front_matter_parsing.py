import unittest
from pathlib import Path
from md_front_matter_parser.markdown_front_matter_parser import MarkdownFrontMatterParser
from md_front_matter_parser.markdown_file import MarkdownFile
from md_front_matter_parser.invalid_markdown_exception import InvalidMarkdownException

class TestSongService(unittest.TestCase):
    def setUp(self):
        self.md_parser = MarkdownFrontMatterParser()
        self.fixtures_dir = Path(__file__).parent / "fixtures"

    def test_able_to_parse_markdown_with_no_body(self):
        file_path = self.fixtures_dir / 'drive.md'
        md_file = self.md_parser.parse(file_path)

        self.assertEqual(md_file.path, file_path)
        self.assertEqual(md_file.body, '')
        self.assertEqual(md_file.front_matter, {'name': 'Drive', 'artist': 'Incubus', 'skill': '2'})

    def test_able_to_parse_markdown_with_body(self):
        file_path = self.fixtures_dir / 'song_with_body.md'
        md_file = self.md_parser.parse(file_path)

        self.assertEqual(md_file.path, file_path)
        self.assertEqual(md_file.body, 'data lies here\n<h1>hello world</h1>\n\nteehee\n')
        self.assertEqual(md_file.front_matter, {'name': 'Wild World', 'artist': 'Cat Stevens', 'skill': '3'})

    def test_raises_exception_for_malformed_front_matter(self):
        file_path = self.fixtures_dir / 'malformed_front_matter.md'

        self.assertRaises(InvalidMarkdownException, self.md_parser.parse, file_path)

    def test_raises_exception_for_non_markdown_files(self):
        file_path = self.fixtures_dir / 'text_file.txt'

        self.assertRaises(InvalidMarkdownException, self.md_parser.parse, file_path)

    def test_raises_exception_for_empty_file(self):
        file_path = self.fixtures_dir / 'empty_file.md'

        self.assertRaises(InvalidMarkdownException, self.md_parser.parse, file_path)

    def test_raises_exception_for_multiline_front_matter_property(self):
        file_path = self.fixtures_dir / 'front_matter_with_array.md'

        self.assertRaises(InvalidMarkdownException, self.md_parser.parse, file_path)


