from dataclasses import dataclass

from domain.exceptions.base import ApplicationException


@dataclass(eq=True)
class RateNotFoundException(ApplicationException):
    @property
    def message(self):
        return f'Не найдено тарифа'


@dataclass
class UniqueRatesException(ApplicationException):
    @property
    def message(self):
        return f'Тарифы с данной датой и типом груза уже существуют'
