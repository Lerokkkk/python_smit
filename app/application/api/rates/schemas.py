from pydantic import BaseModel, RootModel
from typing import List, Dict
from datetime import date

from domain.entites.rate import RateEntity


class RateItem(BaseModel):
    cargo_type: str
    rate: float


class RatesByDate(RootModel):
    root: Dict[date, List[RateItem]]

    def to_entity(self):
        entities = list()
        for timestamp, rates in self.root.items():
            for r in rates:
                entities.append(RateEntity(cargo_type=r.cargo_type, rate=r.rate, date=timestamp))
        return entities


class RateOut(BaseModel):
    id: int
    date: date
    cargo_type: str
    rate: float
