from contextlib import asynccontextmanager

from aiokafka import AIOKafkaProducer
from fastapi import FastAPI

from application.api.rates.handlers import router as rates_router
from application.api.insurance.handlers import router as insurance_router
from logic import init_container

container = init_container()


@asynccontextmanager
async def lifespan(app: FastAPI):
    producer = container.resolve(AIOKafkaProducer)
    await producer.start()

    yield

    await producer.stop()


def create_app() -> FastAPI:
    app = FastAPI(
        title='Simple Insurance Service',
        docs_url='/api/docs',
        description='A simple service for calculating the cost of insurance',
        debug=True,
        lifespan=lifespan
    )

    app.include_router(rates_router)
    app.include_router(insurance_router)

    return app
