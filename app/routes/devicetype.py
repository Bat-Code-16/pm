from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.models.devicetype import DeviceType
from app.database.schemas.devicetype import DeviceTypeBase

router = APIRouter()

@router.get("/", response_model=List[DeviceTypeBase])
def get_device_types(db: Session = Depends(get_db)):
    device_types = DeviceType.get_all(db)
    if not device_types:
        raise HTTPException(status_code=404, detail="No device types found")
    return device_types
