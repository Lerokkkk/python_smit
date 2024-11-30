import datetime

from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class RateModel(Base):
    __tablename__ = 'rates'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    cargo_type: Mapped[str]
    rate: Mapped[float]
    date: Mapped[datetime.date]

    __table_args__ = (
        UniqueConstraint('cargo_type', 'date', name='cargo_type_date_unique_constraint'),
    )

    def __str__(self):
        return f"Тариф с id: {self.id}, cargo_type: {self.cargo_type}, rate: {self.rate}, date: {self.date}"

    def __repr__(self):
        return f"Тариф с id: {self.id}, cargo_type: {self.cargo_type}, rate: {self.rate}, date: {self.date}"
