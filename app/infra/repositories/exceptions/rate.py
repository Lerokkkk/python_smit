from dataclasses import dataclass

from domain.exceptions.base import ApplicationException


@dataclass(eq=True)
class RateNotFoundException(ApplicationException):
    rate_id: int

    @property
    def message(self):
        return f'Не найдено тарифа с {self.rate_id} id'
