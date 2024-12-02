import datetime
from dataclasses import dataclass

from domain.entites.log import LogEntity
from domain.value_objects.insurance_params import InsuranceParams
from logic.services.insurance_service.base import BaseInsuranceService
from logic.services.logger_service.base import BaseLoggerService


@dataclass
class CalculateInsuranceUseCase:
    insurance_service: BaseInsuranceService
    logger_service: BaseLoggerService

    async def execute(self, params: InsuranceParams, user_id: int | None = None) -> float:
        response_rates = await self.insurance_service.calculate_insurance_cost(params)
        message = LogEntity(user_id=user_id,
                            action='вычисление стоимости страхование',
                            timestamp=datetime.datetime.now())
        await self.logger_service.send_logs(message)
        return response_rates


