from scanner.base.base_scanner import BaseScanner
from scanner.results.keyword_result import KeywordResult


class KeywordScanner(BaseScanner):

    KEYWORDS = [
        "секретно",
        "конфиденциально",
        "конфеденциально",
        "пароль",
        "password",
        "login",
        "логин"
    ]

    def scan(self, context):

        keywords = [
            word
            for word in self.KEYWORDS
            if word.lower() in context.tokens
        ]

        keywords = list(set(keywords))

        return KeywordResult(
            scanner_name="keyword_scanner",
            count=len(keywords),
            keywords=keywords
        )