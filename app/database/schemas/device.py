from pydantic import BaseModel
from uuid import UUID
from typing import Optional


class DeviceResponse(BaseModel):
    deviceid: Optional[UUID] = None
    typeid: Optional[UUID] = None

    # customer_id: UUID

    class Config:
        orm_mode = True
