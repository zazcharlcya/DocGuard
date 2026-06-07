import unittest

from scanner.context.analysis_context import AnalysisContext
from scanner.scanners.card_scanner import CardScanner


class TestCardScanner(unittest.TestCase):

    def setUp(self):
        self.scanner = CardScanner()

    def make_context(self, text):
        return AnalysisContext(
            raw_text=text,
            normalized_text=text,
            tokens=[]
        )

    def test_find_cards(self):
        # Используем настоящие номера карт, проходящие алгоритм Луна
        text = """
        4532 0151 1283 0366
        5425-2334-3010-9903
        4111111111111111
        """

        result = self.scanner.scan(
            self.make_context(text)
        )

        self.assertEqual(result.count, 3)

    def test_empty_text(self):
        result = self.scanner.scan(
            self.make_context("")
        )

        self.assertEqual(result.count, 0)
        self.assertEqual(result.cards, [])


if __name__ == "__main__":
    unittest.main()
