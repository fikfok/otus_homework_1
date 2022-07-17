from fastapi import FastAPI

from otus_homework_1.config import get_settings
from otus_homework_1.openapi import tags_metadata
from routers import routers


app = FastAPI(
    title='OTUS homework 1',
    openapi_tags=tags_metadata,
    docs_url='/docs',
)
app_settings = get_settings()

app.include_router(routers.router)
