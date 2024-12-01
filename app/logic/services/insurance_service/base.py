from abc import ABC, abstractmethod
from dataclasses import dataclass

from domain.value_objects.insurance_params import InsuranceParams


@dataclass
class BaseAsyncInsuranceService(ABC):
    @abstractmethod
    def calculate_insurance_cost(self, insurance_parameters: InsuranceParams) -> float:
        ...
