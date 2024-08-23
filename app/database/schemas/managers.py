from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum

# Define the ManagerType Enum in Pydantic
class ManagerType(str,Enum):
    admin = "admin"
    tenant = "tenant"
    viewer = "viewer"

# Pydantic model for creating a manager
class ManagerCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    type: ManagerType

# Pydantic model for reading a manager (response model)
class ManagerRead(BaseModel):
    id: int
    name: str
    email: EmailStr
    type: ManagerType

    class Config:
        orm_mode = True

# Pydantic model for updating a manager
class ManagerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    type: Optional[ManagerType] = None

# Pydantic model for login
class ManagerLogin(BaseModel):
    email: EmailStr
    password: str
