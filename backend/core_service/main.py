import os

from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from api import visits, sessions, notes, documentations, pairing, recordings, auth, summary
from utils.general import initialize_database
from utils import security
from logger import logger

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specify domains ['http://localhost:3000']
    allow_credentials=True,
    allow_methods=["*"],  # or just ['POST']
    allow_headers=["*"],
)


# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Global exception: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error", "message": str(exc)}
    )


app.include_router(auth.router)
app.include_router(visits.router)
app.include_router(sessions.router)
app.include_router(notes.router)
app.include_router(summary.router)
app.include_router(documentations.router)
app.include_router(pairing.router)
app.include_router(recordings.router)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    username = security.verify_token(token)
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"username": username}


@app.on_event("startup")
async def startup_event():
    db_uri = os.getenv('DATABASE_URL', 'postgresql://navina_user:navina_password@postgres/navina_db')

    # Wait for the database to be ready
    engine = initialize_database(db_uri)

    logger.info("Database is ready")
    logger.info("Starting the application")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
