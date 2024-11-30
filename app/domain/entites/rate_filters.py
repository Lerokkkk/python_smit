from dataclasses import dataclass
import datetime


@dataclass(eq=False)
class RateFiltersEntity:
    cargo_type: str | None = None
    rate: float | None = None
    date: datetime.date | None = None
