from fastapi import APIRouter, HTTPException, status
from utils import security
from pydantic import BaseModel

router = APIRouter()


class Token(BaseModel):
    access_token: str
    token_type: str


class LoginData(BaseModel):
    username: str
    password: str


@router.post("/token", response_model=Token)
async def login_for_access_token(login_data: LoginData):
    if security.authenticate_user(login_data.username, login_data.password):
        access_token = security.create_access_token(login_data.username)
        return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )
