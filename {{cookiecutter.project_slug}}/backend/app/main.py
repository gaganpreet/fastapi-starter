from fastapi import FastAPI
from app.core.config import settings
from app.core.logger import logger
from app.api import api_router

description = f"{settings.PROJECT_NAME} API"
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_PATH}/openapi.json",
    docs_url="/docs/",
    description=description,
    redoc_url=None,
)

app.include_router(api_router, prefix=settings.API_PATH)

if __name__ == "__main__":
    import uvicorn

    logger.info("Starting uvicorn in reload mode")
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=5000)
