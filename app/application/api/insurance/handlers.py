from fastapi import Depends, HTTPException
from fastapi.routing import APIRouter

from application.api.dependencies import build_calculate_insurance_cost_use_case
from application.api.insurance.schemas import InsuranceParamsIn, InsuranceCostOut
from domain.exceptions.base import ApplicationException
from logic import CalculateInsuranceUseCase

router = APIRouter(tags=['insurance'])


@router.post('/insurance/', response_model=InsuranceCostOut)
async def calculate_cost_handler(insurance_params: InsuranceParamsIn,
                                 user_id: int | None = None,
                                 use_case: CalculateInsuranceUseCase = Depends(
                                     build_calculate_insurance_cost_use_case)):
    try:
        print("Параметры: ", insurance_params)
        response = await use_case.execute(insurance_params.to_entity(), user_id)
        return InsuranceCostOut(cost=response)
    except ApplicationException as e:
        raise HTTPException(status_code=404, detail=e.message)
