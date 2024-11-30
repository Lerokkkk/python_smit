from abc import ABC, abstractmethod
from dataclasses import dataclass

from app.domain.entites.rate import RateEntity
from domain.entites.rate_filters import RateFiltersEntity
from domain.entites.rate_update import RateUpdateEntity


@dataclass
class BaseRateRepository(ABC):
    @abstractmethod
    def add_rates(self, rates: list[RateEntity]):
        """Добавляет один или несколько тарифов"""
        ...

    @abstractmethod
    def get_rate_by_id(self, rate_id: int):
        """Получает тариф по идентификатору"""
        ...

    @abstractmethod
    def get_rates_by_filters(self, filters: RateFiltersEntity):
        ...

    @abstractmethod
    def update_rate(self, update_fields: RateUpdateEntity):
        """Обновить тариф по идентификатору"""
        ...

    @abstractmethod
    def delete_rate(self, rate_id: int):
        ...
