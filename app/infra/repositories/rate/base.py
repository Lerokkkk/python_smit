from abc import ABC, abstractmethod
from dataclasses import dataclass

from domain.entites.rate import RateEntity
from domain.entites.rate_filters import RateFiltersEntity


@dataclass
class BaseRateRepository(ABC):

    @abstractmethod
    async def get_actual_rate(self, filters: RateFiltersEntity) -> RateEntity:
        ...

    @abstractmethod
    async def add_rates(self, rates: list[RateEntity]):
        """Добавить тарифы"""
        ...

    @abstractmethod
    async def get_rates_by_filters(self, filters: RateFiltersEntity):
        """Получить тарифы по фильтрам"""
        ...

    @abstractmethod
    async def get_all_rates(self):
        """Получить все тарифы"""
        ...

    @abstractmethod
    async def update_rates(self, rates: list[RateEntity]):
        """Обновить тарифы"""
        ...

    @abstractmethod
    async def delete_rates(self, rates: list[RateEntity]):
        """Удалить тарифы"""
        ...
