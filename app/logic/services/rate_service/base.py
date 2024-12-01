from abc import ABC, abstractmethod

from domain.entites.rate import RateEntity
from domain.entites.rate_filters import RateFiltersEntity


class BaseRateService(ABC):
    @abstractmethod
    async def add_rates(self, rates: list[RateEntity]) -> list[RateEntity]:
        ...

    @abstractmethod
    async def get_all_rates(self) -> list[RateEntity]:
        ...

    @abstractmethod
    async def get_rates_by_filters(self, filters: RateFiltersEntity) -> list[RateEntity]:
        ...

    @abstractmethod
    async def update_rates(self, rates: list[RateEntity]) -> str:
        ...

    @abstractmethod
    async def delete_rates(self, rates: list[RateEntity]) -> str:
        ...
