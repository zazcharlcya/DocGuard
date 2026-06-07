import re

import docx as python_docx
import pdfplumber

from scanner.pipeline.scanner_pipeline import (
    ScannerPipeline
)


class FileScanner:

    def __init__(self, pipeline):

        self.pipeline = pipeline

    def read_file(self, file_path):
        ext = file_path.rsplit(".", 1)[-1].lower()
        if ext == "docx":
            doc = python_docx.Document(file_path)
            return "\n".join(p.text for p in doc.paragraphs)
        elif ext == "pdf":
            pages = []
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    text = page.extract_text()
                    if text:
                        pages.append(text)
            return "\n".join(pages)
        else:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
                return file.read()

    def normalize_text(self, text):

        return re.sub(
            r"\s+",
            " ",
            text
        )

    def scan_file(self, file_path):

        text = self.read_file(file_path)

        normalized_text = self.normalize_text(text)

        return self.pipeline.run(
            normalized_text
        )
