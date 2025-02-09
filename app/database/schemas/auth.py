from typing import Optional
from pydantic import BaseModel, EmailStr, conint
from datetime import datetime


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None