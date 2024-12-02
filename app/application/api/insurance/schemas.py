from datetime import date

from pydantic import BaseModel

from domain.value_objects.insurance_params import InsuranceParams


class InsuranceParamsIn(BaseModel):
    cargo_type: str
    date: date
    declared_value: float

    def to_entity(self):
        return InsuranceParams(cargo_type=self.cargo_type,
                               date=self.date,
                               declared_value=self.declared_value)


class InsuranceCostOut(BaseModel):
    cost: float
