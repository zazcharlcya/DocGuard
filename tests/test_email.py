import unittest

from scanner.context.analysis_context import AnalysisContext
from scanner.scanners.email_scanner import EmailScanner


class TestEmailScanner(unittest.TestCase):

    def setUp(self):
        self.scanner = EmailScanner()

    def make_context(self, text):
        return AnalysisContext(
            raw_text=text,
            normalized_text=text,
            tokens=[]
        )

    def test_find_emails(self):
        text = """
        test@gmail.com
        admin@mail.ru
        invalid@email
        """

        result = self.scanner.scan(
            self.make_context(text)
        )

        self.assertIn("test@gmail.com", result.emails)
        self.assertIn("admin@mail.ru", result.emails)
        self.assertEqual(result.count, 2)

    def test_empty_text(self):
        result = self.scanner.scan(
            self.make_context("")
        )

        self.assertEqual(result.count, 0)
        self.assertEqual(result.emails, [])


if __name__ == "__main__":
    unittest.main()