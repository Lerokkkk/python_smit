from functools import lru_cache
from punq import Container, Scope
from aiokafka import AIOKafkaProducer

from infra.repositories.rate.base import BaseRateRepository
from infra.repositories.rate.orm import ORMRateRepository
from logic.services.insurance_service.base import BaseInsuranceService
from logic.services.insurance_service.insurance import InsuranceService
from logic.services.logger_service.base import BaseLoggerService
from logic.services.logger_service.kafka import KafkaLoggingService
from logic.services.rate_service.base import BaseRateService
from logic.services.rate_service.rate import RateService
from logic.use_cases.insurance.calculate_cost import CalculateInsuranceUseCase
from logic.use_cases.rates.create import CreateRateUseCase
from logic.use_cases.rates.delete import DeleteRatesUseCase
from logic.use_cases.rates.get import GetRatesUseCase
from logic.use_cases.rates.update import UpdateRatesUseCase


@lru_cache(1)
def init_container():
    return _init_container()


def _init_container() -> Container:
    container = Container()

    container = Container()

    container.register(BaseRateRepository, factory=lambda: ORMRateRepository(None))

    container.register(BaseRateService, factory=lambda: RateService(container.resolve(BaseRateRepository)))
    container.register(BaseLoggerService, factory=lambda: KafkaLoggingService(container.resolve(AIOKafkaProducer)))
    container.register(BaseInsuranceService, factory=lambda: InsuranceService(container.resolve(BaseRateRepository)))

    container.register(
        CalculateInsuranceUseCase,
        factory=lambda: CalculateInsuranceUseCase(
            insurance_service=container.resolve(BaseInsuranceService),
            logger_service=container.resolve(BaseLoggerService),
        ),
    )

    container.register(
        CreateRateUseCase,
        factory=lambda: CreateRateUseCase(
            rate_service=container.resolve(BaseRateService),
            logger_service=container.resolve(BaseLoggerService),
        ),
    )

    container.register(
        GetRatesUseCase,
        factory=lambda: GetRatesUseCase(
            rate_service=container.resolve(BaseRateService),
            logger_service=container.resolve(BaseLoggerService),
        ),
    )

    container.register(
        UpdateRatesUseCase,
        factory=lambda: UpdateRatesUseCase(
            rate_service=container.resolve(BaseRateService),
            logger_service=container.resolve(BaseLoggerService),
        ),
    )

    container.register(
        DeleteRatesUseCase,
        factory=lambda: DeleteRatesUseCase(
            rate_service=container.resolve(BaseRateService),
            logger_service=container.resolve(BaseLoggerService),
        ),
    )

    def init_kafka_producer():
        return AIOKafkaProducer(
            bootstrap_servers="kafka:29092",
            max_batch_size=512,
            linger_ms=100

        )

    container.register(AIOKafkaProducer, factory=init_kafka_producer, scope=Scope.singleton)

    return container
