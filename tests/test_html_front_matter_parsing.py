import unittest
from pathlib import Path
from md_front_matter_parser.front_matter_parser_factory import FrontMatterParserFactory

class TestHTMLFrontMatterParsing(unittest.TestCase):
    def setUp(self):
        self.parser_factory = FrontMatterParserFactory()
        self.fixtures_dir = Path(__file__).parent / "fixtures"

    def test_able_to_parse_html_with_no_content(self):
        file_path = self.fixtures_dir / 'no_content_post.html'
        html_parser = self.parser_factory.get_parser(file_path)
        html_file = html_parser.parse()

        self.assertEqual(html_file.path, file_path)
        self.assertEqual(html_file.content, None)
        self.assertEqual(html_file.front_matter, {'category': 'cooking', 'title': 'Lord of the Rings'})

    def test_able_to_parse_html_with_content(self):
        file_path = self.fixtures_dir / 'blog_post.html'
        html_parser = self.parser_factory.get_parser(file_path)
        html_file = html_parser.parse()

        self.assertEqual(html_file.path, file_path)
        self.assertEqual(html_file.content.raw_content, '\n<h1>Onion Ringz</h1>\n<p>Love that content</p>\n')
        self.assertEqual(html_file.front_matter, {'category': 'cooking', 'title': 'Lord of the Rings'})

