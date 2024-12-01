import datetime
from dataclasses import dataclass

from domain.entites.log import LogEntity
from domain.entites.rate import RateEntity
from logic.services.logger_service.base import BaseLoggerService
from logic.services.rate_service.base import BaseRateService


@dataclass
class GetRatesUseCase:
    rate_service: BaseRateService
    logger_service: BaseLoggerService

    async def execute(self, user_id: int | None = None) -> list[RateEntity]:
        response_rates = await self.rate_service.get_all_rates()
        message = LogEntity(user_id=user_id,
                            action='получение записей',
                            timestamp=datetime.datetime.now())
        await self.logger_service.send_logs(message)

        return response_rates
