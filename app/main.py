from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html

import model
from routes import router

from config import engine

model.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get('/')
async def home():
    return "За 100 рублей сделаю свой fastapi без orm и крудами"


app.include_router(router, prefix="/users", tags=["users"])
app.include_router(router, prefix="/auth", tags=["auth"])
app.include_router(router, prefix="/cards", tags=["cards"])
app.include_router(router, prefix="/sessions", tags=["sessions"])
app.include_router(router, prefix="/transports", tags=["transports"])
app.include_router(router, prefix="/snils", tags=["snils"])


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="Custom Swagger UI"
    )


@app.get("/openapi.json", include_in_schema=False)
async def get_openapi():
    return app.openapi()
