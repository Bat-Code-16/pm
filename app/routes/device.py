from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID
from app.models.device import Device
from app.database.schemas.device import DeviceResponse
from app.core.database import get_db

router = APIRouter()

@router.get("/{device_id}", response_model=DeviceResponse)
def get_device(device_id: UUID, db: Session = Depends(get_db)):
    # Query for the device with the specified ID
    device = db.query(Device.deviceid, Device.typeid).filter(Device.deviceid == device_id).first()

    if not device:
        # Return 404 Not Found if the device does not exist
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Device with ID {device_id} does not exist"
        )

    return device
