from fastapi import FastAPI, HTTPException, Depends
from api.routes import router
from utils.redis_manager import redis_manager
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(router)


@app.on_event("startup")
async def startup_event():
    try:
        await redis_manager.init_redis_client()
        if not await redis_manager.check_redis_connection():
            raise HTTPException(status_code=500, detail="Failed to connect to Redis")
        logger.info("Server started successfully")
    except Exception as e:
        logger.error(f"Failed to start server: {str(e)}")
        raise


@app.on_event("shutdown")
async def shutdown_event():
    await redis_manager.close_redis_client()


@app.get("/healthcheck")
async def healthcheck():
    if await redis_manager.check_redis_connection():
        return {"status": "healthy"}
    else:
        raise HTTPException(status_code=500, detail="Redis connection failed")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)
