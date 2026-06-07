import re

from scanner.base.base_scanner import BaseScanner
from scanner.results.card_result import CardResult


def luhn_check(number: str) -> bool:
    """
    Алгоритм Луна — валидация номера платёжной карты.
    Возвращает True, если контрольная сумма корректна.
    """
    digits = [int(d) for d in number if d.isdigit()]

    if len(digits) < 13 or len(digits) > 19:
        return False

    total = 0
    for i, digit in enumerate(reversed(digits)):
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit

    return total % 10 == 0


class CardScanner(BaseScanner):
    """
    Детектор номеров банковских карт с проверкой
    по алгоритму Луна (отсеивает случайные последовательности цифр).
    """

    CARD_PATTERN = re.compile(
        r"\b(?:\d{4}[\s\-]?){3}\d{4}\b"
    )

    def scan(self, context):

        candidates = self.CARD_PATTERN.findall(
            context.normalized_text
        )

        # Только те, что прошли алгоритм Луна
        cards = list({
            c.strip()
            for c in candidates
            if luhn_check(c)
        })

        return CardResult(
            scanner_name="card_scanner",
            count=len(cards),
            cards=cards
        )
