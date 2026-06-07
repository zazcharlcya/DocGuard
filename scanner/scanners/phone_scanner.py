import re

from scanner.base.base_scanner import BaseScanner
from scanner.results.phone_result import PhoneResult


class PhoneScanner(BaseScanner):
    """
    Детектор российских телефонных номеров.
    Поддерживает форматы:
        +7 (999) 123-45-67
        8 999 123 45 67
        +79991234567
        89991234567
    """

    PHONE_PATTERN = re.compile(
        r"""
        (?<!\d)              # не цифра слева
        (?:\+7|8)            # код страны
        [\s\-\(]*            # пробелы/скобки
        \d{3}                # код оператора
        [\s\-\)]*
        \d{3}
        [\s\-]*
        \d{2}
        [\s\-]*
        \d{2}
        (?!\d)               # не цифра справа
        """,
        re.VERBOSE | re.MULTILINE
    )

    def scan(self, context):

        matches = self.PHONE_PATTERN.findall(
            context.normalized_text
        )

        phones = list({m.strip() for m in matches})

        return PhoneResult(
            scanner_name="phone_scanner",
            count=len(phones),
            phones=phones
        )
