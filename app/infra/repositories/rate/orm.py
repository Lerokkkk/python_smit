import datetime
from dataclasses import fields

from fastapi import Depends
from sqlalchemy import and_, select

from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from domain.entites.rate_filters import RateFiltersEntity
from domain.entites.rate_update import RateUpdateEntity
from domain.exceptions.base import ApplicationException
from infra.repositories.exceptions.rate import RateNotFoundException
from infra.repositories.models.db import get_db
from infra.repositories.models.rate import RateModel
from infra.repositories.rate.conventers import convert_rate_to_dict, convert_rate_model_to_entity

from app.domain.entites.rate import RateEntity

from app.infra.repositories.rate.base import BaseRateRepository


class ORMRateRepository(BaseRateRepository):
    def __init__(self, session: AsyncSession):

        self.session = session

    def _query_builder(self, filters: RateFiltersEntity):
        response_filters = list()
        for field in fields(filters):
            if getattr(filters, field.name) is not None:
                value = getattr(filters, field.name)
                field_attr = getattr(RateModel, field.name)
                response_filters.append(field_attr == value)
        return response_filters

    async def add_rates(self, rates: list[RateEntity]) -> list[RateEntity]:
        rates_to_add = [convert_rate_to_dict(obj) for obj in rates]
        stmt = insert(RateModel).values(rates_to_add).returning(RateModel)

        result = await self.session.scalars(stmt)
        rates_from_db = result.all()
        response = [convert_rate_model_to_entity(obj) for obj in rates_from_db]
        await self.session.commit()
        return response

    async def get_rate_by_id(self, rate_id: int) -> RateEntity:
        rate_model = await self.session.get(RateModel, rate_id)
        if not rate_model:
            raise RateNotFoundException(rate_id)
        return convert_rate_model_to_entity(rate_model)

    async def get_rates_by_filters(self, filters: RateFiltersEntity) -> list[RateEntity]:
        built_filters = self._query_builder(filters)
        stmt = select(RateModel)
        stmt = stmt.where(and_(True, *built_filters))

        result = await self.session.execute(stmt)
        rates = result.scalars().all()
        return [convert_rate_model_to_entity(obj) for obj in rates]

    async def update_rate(self, update_fields: RateUpdateEntity) -> RateEntity:
        rate_model = await self.session.get(RateModel, update_fields.id)
        if not rate_model:
            raise RateNotFoundException(update_fields.id)

        for field in fields(update_fields):
            if getattr(update_fields, field.name) is not None and field.name != 'id':
                value = getattr(update_fields, field.name)
                setattr(rate_model, field.name, value)

        await self.session.commit()
        return convert_rate_model_to_entity(rate_model)

    async def delete_rate(self, rate_id: int) -> RateEntity:
        rate_model = await self.session.get(RateModel, rate_id)
        if not rate_model:
            raise RateNotFoundException(rate_id)

        await self.session.delete(rate_model)
        await self.session.commit()

        return convert_rate_model_to_entity(rate_model)
