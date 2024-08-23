from passlib.context import CryptContext
import bcrypt
from fastapi import Request, HTTPException, Depends
from typing import Union
from fastapi.security import OAuth2PasswordRequestForm
from app.database.schemas.managers import ManagerLogin
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password: str):
    return pwd_context.hash(password)


def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)



# async def parse_manager_credentials(request: Request) -> Union[ManagerLogin, OAuth2PasswordRequestForm]:
#     content_type = request.headers.get('Content-Type')

#     if content_type == 'application/json':
#         data = await request.json()
#         return ManagerLogin(**data)
#     elif content_type == 'application/x-www-form-urlencoded':
#         form = await request.form()
#         return OAuth2PasswordRequestForm(username=form.get('username'), password=form.get('password'))
#     else:
#         raise HTTPException(status_code=415, detail="Unsupported Media Type")
