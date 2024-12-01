from contextlib import asynccontextmanager

from aiokafka import AIOKafkaProducer
from fastapi import FastAPI, APIRouter

from application.api.rates.handlers import router
from logic import init_container

container = init_container()


@asynccontextmanager
async def lifespan(app: FastAPI):
    producer = container.resolve(AIOKafkaProducer)
    await producer.start()

    yield
    # Clean up the ML models and release the resources
    await producer.stop()


def create_app() -> FastAPI:
    app = FastAPI(
        title='Simple Kafka Chat',
        docs_url='/api/docs',
        description='A simple kafka + ddd example.',
        debug=True,
        lifespan=lifespan
    )

    app.include_router(router)

    return app
