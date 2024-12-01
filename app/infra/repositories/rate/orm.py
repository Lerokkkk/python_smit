from dataclasses import fields

from asyncpg import UniqueViolationError
from sqlalchemy import and_, select, update, bindparam, delete
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from domain.entites.rate import RateEntity
from domain.entites.rate_filters import RateFiltersEntity
from infra.repositories.exceptions.rate import RateNotFoundException, UniqueRatesException
from infra.repositories.models.rate import RateModel
from infra.repositories.rate.base import BaseRateRepository
from infra.repositories.rate.conventers import convert_rate_to_dict, convert_rate_model_to_entity


class ORMRateRepository(BaseRateRepository):
    def __init__(self, session: AsyncSession | None):

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

        try:
            stmt = insert(RateModel).values(rates_to_add).returning(RateModel)

            result = await self.session.scalars(stmt)
            rates_from_db = result.all()
            response = [convert_rate_model_to_entity(obj) for obj in rates_from_db]
            await self.session.commit()
            return response
        except (IntegrityError, UniqueViolationError) as e:
            await self.session.rollback()
            raise UniqueRatesException()

    async def get_all_rates(self) -> list[RateEntity]:
        result = await self.session.execute(select(RateModel))
        return [convert_rate_model_to_entity(obj) for obj in result.scalars().all()]

    async def get_rates_by_filters(self, filters: RateFiltersEntity) -> list[RateEntity]:
        built_filters = self._query_builder(filters)
        stmt = select(RateModel)
        stmt = stmt.where(and_(True, *built_filters))

        result = await self.session.execute(stmt)
        rates = result.scalars().all()
        return [convert_rate_model_to_entity(obj) for obj in rates]

    async def update_rates(self, rates: list[RateEntity]) -> str:
        data_for_update = [
            {
                "b_date": rate.date,
                "b_cargo_type": rate.cargo_type,
                "rate": rate.rate
            }
            for rate in rates
        ]
        async with self.session.begin():
            connection = await self.session.connection()
            stmt = (
                update(RateModel).where(RateModel.date == bindparam("b_date"),
                                        RateModel.cargo_type == bindparam("b_cargo_type"))
            )
            await connection.execute(stmt, data_for_update)
            await self.session.commit()
        return "Success"

    async def delete_rates(self, rates: list[RateEntity]) -> str:
        data_for_update = [
            {
                "b_date": rate.date,
                "b_cargo_type": rate.cargo_type,
                "rate": rate.rate
            }
            for rate in rates
        ]
        async with self.session.begin():
            connection = await self.session.connection()
            stmt = (
                delete(RateModel).where(RateModel.date == bindparam("b_date"),
                                        RateModel.cargo_type == bindparam("b_cargo_type"))
            )
            await connection.execute(stmt, data_for_update)
            await self.session.commit()
        return "Success"

    async def get_actual_rate(self, filters: RateFiltersEntity) -> RateEntity:
        query = (select(RateModel).filter(
            RateModel.cargo_type == filters.cargo_type,
            RateModel.date <= filters.date
        )
                 .order_by(RateModel.date.desc())
                 .limit(1)
                 )
        result = await self.session.execute(query)
        response = result.scalar_one_or_none()
        if not response:
            raise RateNotFoundException()
        return convert_rate_model_to_entity(response)


# async def main():
#     rates = [
#         RateModel(date=date(2024, 6, 1), cargo_type="Glass", rate=0.047),
#         RateModel(date=date(2024, 6, 1), cargo_type="Other", rate=0.01),
#         RateModel(date=date(2024, 7, 1), cargo_type="Glass", rate=0.035),
#         RateModel(date=date(2024, 7, 1), cargo_type="Other", rate=0.022),
#     ]
#     async with async_session() as session:
#         r = ORMRateRepository(session=session)
#         response = await r.add_rates(rates)
#         print(response)


