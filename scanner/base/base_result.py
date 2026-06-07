from dataclasses import dataclass


@dataclass(frozen=True)
class BaseResult:

    scanner_name: str

    count: int