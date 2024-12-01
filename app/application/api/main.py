from fastapi import FastAPI, APIRouter


def create_app() -> FastAPI:
    app = FastAPI(
        title='Simple Kafka Chat',
        docs_url='/api/docs',
        description='A simple kafka + ddd example.',
        debug=True,
    )
    router = APIRouter(tags=['Chat'])

    @router.get('/')
    async def ping():
        return "pong"
    app.include_router(router)

    return app
