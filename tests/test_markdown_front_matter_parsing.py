import unittest
from pathlib import Path
from markup_front_matter_parser.front_matter_parser_factory import FrontMatterParserFactory

class TestMarkdownFrontMatterParsing(unittest.TestCase):
    def setUp(self):
        self.parser_factory = FrontMatterParserFactory()
        self.fixtures_dir = Path(__file__).parent / "fixtures"

    def test_able_to_parse_markdown_with_no_content(self):
        file_path = self.fixtures_dir / 'drive.md'
        md_parser = self.parser_factory.get_parser(file_path)
        md_file = md_parser.parse()

        self.assertEqual(md_file.path, file_path)
        self.assertEqual(md_file.content, None)
        self.assertEqual(md_file.front_matter, {'name': 'Drive', 'artist': 'Incubus', 'skill': '2'})

    def test_able_to_parse_markdown_with_content(self):
        file_path = self.fixtures_dir / 'song_with_body.md'
        md_parser = self.parser_factory.get_parser(file_path)
        md_file = md_parser.parse()

        self.assertEqual(md_file.path, file_path)
        self.assertEqual(md_file.content.raw, 'data lies here\n<h1>hello world</h1>\n\nteehee\n')
        self.assertEqual(md_file.front_matter, {'name': 'Wild World', 'artist': 'Cat Stevens', 'skill': '2'})

