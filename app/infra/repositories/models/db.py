import asyncio
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from infra.repositories.models.rate import Base
from settings.config import config

engine = create_async_engine(
    f"postgresql+asyncpg://{config.db_user}:{config.db_password}@{config.db_host}:{config.outside_port}/{config.db_name}"
)

async_session = async_sessionmaker(engine, class_=AsyncSession)


async def get_db() -> AsyncGenerator:
    async with async_session() as session:
        yield session


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(create_tables())

