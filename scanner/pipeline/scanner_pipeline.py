import re

from scanner.context.analysis_context import AnalysisContext
from scanner.preprocessing.text_tokenizer import TextTokenizer


class ScannerPipeline:

    def __init__(self):
        self.scanners = []
        self.tokenizer = TextTokenizer()

    def add_scanner(self, scanner):
        self.scanners.append(scanner)

    def create_context(self, text: str) -> AnalysisContext:
        normalized_text = re.sub(r"\s+", " ", text)
        tokens = self.tokenizer.tokenize(normalized_text)

        return AnalysisContext(
            raw_text=text,
            normalized_text=normalized_text,
            tokens=tokens
        )

    def run(self, text: str):
        if not self.scanners:
            print("WARNING: pipeline has no scanners")

        context = self.create_context(text)

        results = []

        for scanner in self.scanners:
            result = scanner.scan(context)

            if result is not None:
                results.append(result)

        return results