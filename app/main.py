from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from art import tprint
import model
from routes import router

from config import engine

model.Base.metadata.create_all(bind=engine)
app = FastAPI()


# Заголовок панели
@app.on_event("startup")
async def startup():
    tprint("Singletons",space=10)



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


@app.get("/openapi.json", include_in_schema=False)
async def get_openapi():
    return app.openapi()
