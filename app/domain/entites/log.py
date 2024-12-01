from dataclasses import dataclass
import datetime


@dataclass(eq=False)
class LogEntity:
    action: str
    timestamp: datetime
    user_id: int | None = None
