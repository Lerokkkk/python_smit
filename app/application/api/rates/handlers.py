from fastapi import Depends, HTTPException
from fastapi.routing import APIRouter

from application.api.dependencies import get_create_rates_use_case, get_rates_use_case, update_rates_use_case, \
    delete_rates_use_case
from application.api.rates.schemas import RatesByDate, RateOut
from domain.exceptions.base import ApplicationException
from logic import CreateRateUseCase, GetRatesUseCase, UpdateRatesUseCase

router = APIRouter(tags=['rates'])


@router.post('/rates/', response_model=list[RateOut])
async def create_rates_handler(rates_by_date: RatesByDate,
                               user_id: int | None = None,
                               use_case: CreateRateUseCase = Depends(get_create_rates_use_case)):
    try:

        response = await use_case.execute(rates_by_date.to_entity(), user_id)
        return response
    except ApplicationException as e:
        raise HTTPException(status_code=404, detail=e.message)


@router.get('/rates/', response_model=list[RateOut])  # TODO: add filters in query params
async def get_rates_handler(use_case: GetRatesUseCase = Depends(get_rates_use_case), user_id: int | None = None):
    response = await use_case.execute(user_id)

    return response


@router.patch('/rates/')
async def update_rates_handler(rates_by_date: RatesByDate,
                               use_case: UpdateRatesUseCase = Depends(update_rates_use_case),
                               user_id: int | None = None):
    try:

        response = await use_case.execute(rates_by_date.to_entity(), user_id)
        return response
    except ApplicationException as e:
        raise HTTPException(status_code=404, detail=e.message)


@router.delete('/rates/')
async def update_rates_handler(rates_by_date: RatesByDate,
                               use_case: UpdateRatesUseCase = Depends(delete_rates_use_case),
                               user_id: int | None = None):
    try:

        response = await use_case.execute(rates_by_date.to_entity(), user_id)
        return response
    except ApplicationException as e:
        raise HTTPException(status_code=404, detail=e.message)
