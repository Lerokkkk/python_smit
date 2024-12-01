import datetime
from dataclasses import dataclass

from domain.entites.log import LogEntity
from domain.entites.rate import RateEntity
from logic.services.logger_service.base import BaseLoggerService
from logic.services.rate_service.base import BaseRateService


@dataclass
class CreateRateUseCase:
    rate_service: BaseRateService
    logger_service: BaseLoggerService

    async def execute(self, rates: list[RateEntity], user_id: int | None = None) -> list[RateEntity]:
        response_rates = await self.rate_service.add_rates(rates)
        message = LogEntity(user_id=user_id,
                            action='добавление записей',
                            timestamp=datetime.datetime.now())
        await self.logger_service.send_logs(message)

        return response_rates

