from pydantic import BaseModel
from typing import List, Optional
import uuid

class FeaturesBase(BaseModel):
    device_type_id: uuid.UUID
    names: List[str]
    alias: Optional[List[str]] = None
    valid_ranges: Optional[List[str]] = None

class FeaturesCreate(FeaturesBase):
    pass

class FeaturesUpdate(BaseModel):
    names: List[str]
    alias: Optional[List[str]] = None
    valid_ranges: Optional[List[str]] = None

class Features(FeaturesBase):
    id: int

    class Config:
        orm_mode = True
