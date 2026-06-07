import re


class TextTokenizer:

    def tokenize(self, text: str) -> list[str]:

        text = text.lower()

        words = re.findall(
            r"[a-zA-Zа-яА-ЯёЁ]+",
            text
        )

        tokens = [
            word
            for word in words
            if len(word) >= 4
        ]

        return tokens