from dataclasses import dataclass

from domain.entites.rate import RateEntity
from domain.entites.rate_filters import RateFiltersEntity
from infra.repositories.rate.base import BaseRateRepository
from logic.services.rate_service.base import BaseRateService


@dataclass
class RateService(BaseRateService):
    repository: BaseRateRepository

    async def add_rates(self, rates: list[RateEntity]) -> list[RateEntity]:
        return await self.repository.add_rates(rates)

    async def get_all_rates(self) -> list[RateEntity]:
        return await self.repository.get_all_rates()

    async def get_rates_by_filters(self, filters: RateFiltersEntity) -> list[RateEntity]:
        return await self.repository.get_rates_by_filters(filters)

    async def update_rates(self, rates: list[RateEntity]) -> str:
        return await self.repository.update_rates(rates)

    async def delete_rates(self, rates: list[RateEntity]) -> str:
        return await self.repository.delete_rates(rates)
