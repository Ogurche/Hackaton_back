from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from fastapi.openapi.utils import get_openapi
from art import tprint
import model
from routes import router

from config import engine

model.Base.metadata.create_all(bind=engine)
app = FastAPI(
title="Singletons",
    description="Задача 1 - Идентификация держателя Единой карты",
    summary="Разработанный сервис который поможет партнерам проекта «Единая карта жителя Мурманской области» определить индивидуальные скидки, льготы обладателя карты, в офлайн и онлайн режиме.",
    version="0.0.1",

)


# Заголовок панели
@app.on_event("startup")
async def startup():
    tprint("Singletons",space=5)



@app.get('/')
async def home():
    return "За 100 рублей сделаю свой fastapi без orm и крудами"


app.include_router(router, tags=["CRUD"])


# Swagger UI и OpenAPI документация
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="Custom Swagger UI"
    )

@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url="/openapi.json",
        title="ReDoc"
    )

@app.get("/openapi.json", include_in_schema=False)
async def get_open_api_endpoint():
    return get_openapi(
        title="OpenAPI",
        version="1.0.0",
        description="OpenAPI schema",
        routes=app.routes,
    )
