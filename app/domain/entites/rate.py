from dataclasses import dataclass
import datetime


@dataclass(eq=False)
class RateEntity:
    cargo_type: str
    rate: float
    date: datetime.date

    id: int | None = None
