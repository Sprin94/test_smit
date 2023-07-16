import uvicorn
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.api.rates import router
from app.core.config import settings
from app.utils import load_rates

app = FastAPI()
app.include_router(router)


register_tortoise(
    app,
    db_url=settings.POSTGRES_DATABASE_URI,
    modules={'models': ['app.services.database.models']},
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.on_event('startup')
async def on_startup() -> None:
    await load_rates()


def main():
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)


if __name__ == '__main__':
    main()
