from abc import ABC, abstractmethod
from dataclasses import dataclass

from domain.entites.rate_filters import RateFiltersEntity
from domain.entites.rate_update import RateUpdateEntity

from app.domain.entites.rate import RateEntity


@dataclass
class BaseRateRepository(ABC):
    @abstractmethod
    def add_rates(self, rates: list[RateEntity]):
        """Добавить тарифы"""
        ...

    @abstractmethod
    def get_rates_by_filters(self, filters: RateFiltersEntity):
        """Получить тарифы по фильтрам"""
        ...

    @abstractmethod
    def get_all_rates(self) -> list[RateEntity]:
        """Получить все тарифы"""
        ...

    @abstractmethod
    def update_rates(self, rates: list[RateEntity]):
        """Обновить тарифы"""
        ...

    @abstractmethod
    def delete_rates(self, rates: list[RateEntity]):
        """Удалить тарифы"""
        ...
