from abc import ABC, abstractmethod
from dataclasses import dataclass

from domain.value_objects.insurance_params import InsuranceParams


@dataclass
class BaseInsuranceService(ABC):
    @abstractmethod
    async def calculate_insurance_cost(self, insurance_parameters: InsuranceParams) -> float:
        ...
