from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from infra.repositories.models.db import get_db
from infra.repositories.rate.base import BaseRateRepository
from infra.repositories.rate.orm import ORMRateRepository
from logic import init_container, CreateRateUseCase, GetRatesUseCase


async def get_create_rates_use_case(
        db: AsyncSession = Depends(get_db)
) -> CreateRateUseCase:
    container = init_container()

    container.register(BaseRateRepository, factory=lambda: ORMRateRepository(db))

    return container.resolve(CreateRateUseCase)


async def get_rates_use_case(
        db: AsyncSession = Depends(get_db)
) -> GetRatesUseCase:
    container = init_container()

    container.register(BaseRateRepository, factory=lambda: ORMRateRepository(db))

    return container.resolve(GetRatesUseCase)
