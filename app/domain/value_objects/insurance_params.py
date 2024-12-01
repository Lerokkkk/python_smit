from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class InsuranceParams:
    cargo_type: str
    date: datetime.date
    declared_value: float

