from dataclasses import dataclass


@dataclass(frozen=True)
class AnalysisContext:
    raw_text: str
    normalized_text: str
    tokens: list[str]