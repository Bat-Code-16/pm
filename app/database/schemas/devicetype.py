from pydantic import BaseModel
from uuid import UUID

class DeviceTypeBase(BaseModel):
    typeid: UUID
    type: str
    label: str

    class Config:
        orm_mode = True


