from dataclasses import dataclass

from scanner.base.base_result import BaseResult


@dataclass(frozen=True)
class CardResult(BaseResult):

    cards: list[str]