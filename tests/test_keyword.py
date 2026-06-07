import unittest

from scanner.context.analysis_context import AnalysisContext
from scanner.scanners.keyword_scanner import KeywordScanner


class TestKeywordScanner(unittest.TestCase):

    def setUp(self):
        self.scanner = KeywordScanner()

    def make_context(self, text):
        tokens = [
            word.lower()
            for word in text.replace(".", "").split()
            if len(word) >= 4
        ]

        return AnalysisContext(
            raw_text=text,
            normalized_text=text,
            tokens=tokens
        )

    def test_find_keywords(self):
        text = """
        Документ секретно.
        Пароль пользователя.
        CVV код карты.
        """

        result = self.scanner.scan(
            self.make_context(text)
        )

        self.assertIn("секретно", result.keywords)
        self.assertIn("пароль", result.keywords)
        self.assertEqual(result.count, 2)

    def test_empty_text(self):
        result = self.scanner.scan(
            self.make_context("")
        )

        self.assertEqual(result.count, 0)
        self.assertEqual(result.keywords, [])


if __name__ == "__main__":
    unittest.main()