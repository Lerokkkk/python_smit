from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from infra.repositories.models.db import get_db
from infra.repositories.rate.base import BaseRateRepository
from infra.repositories.rate.orm import ORMRateRepository
from logic import init_container, CreateRateUseCase, GetRatesUseCase, UpdateRatesUseCase, CalculateInsuranceUseCase
from logic.use_cases.rates.delete import DeleteRatesUseCase


async def build_calculate_insurance_cost_use_case(
        db: AsyncSession = Depends(get_db)
) -> CalculateInsuranceUseCase:
    container = init_container()

    container.register(BaseRateRepository, factory=lambda: ORMRateRepository(db))

    return container.resolve(CalculateInsuranceUseCase)


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


async def update_rates_use_case(
        db: AsyncSession = Depends(get_db)
) -> UpdateRatesUseCase:
    container = init_container()

    container.register(BaseRateRepository, factory=lambda: ORMRateRepository(db))

    return container.resolve(UpdateRatesUseCase)


async def delete_rates_use_case(
        db: AsyncSession = Depends(get_db)
) -> DeleteRatesUseCase:
    container = init_container()

    container.register(BaseRateRepository, factory=lambda: ORMRateRepository(db))

    return container.resolve(DeleteRatesUseCase)
