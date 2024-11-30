from dataclasses import dataclass

from domain.entites.rate import RateEntity
from domain.entites.rate_filters import RateFiltersEntity
from domain.entites.rate_update import RateUpdateEntity
from infra.repositories.rate.base import BaseRateRepository
from logic.services.rate_service.base import BaseRateService


@dataclass
class RateService(BaseRateService):
    repository: BaseRateRepository

    async def add_rates(self, rates: list[RateEntity]) -> list[RateEntity]:
        return await self.repository.add_rates(rates)

    async def get_rate_by_id(self, rate_id: int) -> RateEntity:
        return await self.repository.get_rate_by_id(rate_id)

    async def get_rates_by_filters(self, filters: RateFiltersEntity) -> list[RateEntity]:
        return await self.repository.get_rates_by_filters(filters)

    async def update_rate(self, update_fields: RateUpdateEntity) -> RateEntity:
        return await self.repository.update_rate(update_fields)

    async def delete_rate(self, rate_id: int) -> RateEntity:
        return await self.repository.delete_rate(rate_id)
