from app.app import create_app
from app.core.logger import logger

app = create_app()

if __name__ == "__main__":
    import uvicorn

    logger.info("Starting uvicorn in reload mode")
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=5000)
