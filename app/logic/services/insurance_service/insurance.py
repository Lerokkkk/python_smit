from dataclasses import dataclass

from domain.entites.rate_filters import RateFiltersEntity
from domain.value_objects.insurance_params import InsuranceParams
from infra.repositories.rate.base import BaseRateRepository
from logic.services.insurance_service.base import BaseInsuranceService


@dataclass
class InsuranceService(BaseInsuranceService):
    repository: BaseRateRepository

    async def calculate_insurance_cost(self, insurance_parameters: InsuranceParams) -> float:
        filters = RateFiltersEntity(cargo_type=insurance_parameters.cargo_type,
                                    date=insurance_parameters.date)
        actual_rate = await self.repository.get_actual_rate(filters)
        cost = actual_rate.rate * insurance_parameters.declared_value
        return cost
