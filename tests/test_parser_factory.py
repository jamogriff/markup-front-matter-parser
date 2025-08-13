import unittest
from pathlib import Path
from md_front_matter_parser.front_matter_parser_factory import FrontMatterParserFactory
from md_front_matter_parser.parsers.markdown_front_matter_parser import MarkdownFrontMatterParser
from md_front_matter_parser.parsers.html_front_matter_parser import HTMLFrontMatterParser

class TestParserFactory(unittest.TestCase):

    def setUp(self):
        self.parser_factory = FrontMatterParserFactory()
        self.fixtures_dir = Path(__file__).parent / "fixtures"

    def test_factory_returns_correct_parsers(self):
        html_file = self.fixtures_dir / 'blog_post.html'
        md_file = self.fixtures_dir / 'drive.md'
        md_parser = self.parser_factory.get_parser(md_file)
        html_parser = self.parser_factory.get_parser(html_file)

        self.assertIsInstance(md_parser, MarkdownFrontMatterParser)
        self.assertIsInstance(html_parser, HTMLFrontMatterParser)

    def test_raises_exception_for_non_markup_files(self):
        file_path = self.fixtures_dir / 'text_file.txt'

        self.assertRaises(ValueError, self.parser_factory.get_parser, file_path)

    def test_raises_exception_for_non_existent_files(self):
        file_path = self.fixtures_dir / 'nowhere-son.html'

        self.assertRaises(FileNotFoundError, self.parser_factory.get_parser, file_path)

