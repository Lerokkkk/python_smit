from abc import ABC, abstractmethod

from domain.entites.rate import RateEntity
from domain.entites.rate_filters import RateFiltersEntity
from domain.entites.rate_update import RateUpdateEntity


class BaseRateService(ABC):
    @abstractmethod
    def add_rates(self, rates: list[RateEntity]) -> list[RateEntity]:
        ...

    @abstractmethod
    def get_rate_by_id(self, rate_id: int) -> RateEntity:
        ...

    @abstractmethod
    def get_rates_by_filters(self, filters: RateFiltersEntity) -> list[RateEntity]:
        ...

    @abstractmethod
    def update_rate(self, update_fields: RateUpdateEntity) -> RateEntity:
        ...

    @abstractmethod
    def delete_rate(self, rate_id: int) -> RateEntity:
        ...


