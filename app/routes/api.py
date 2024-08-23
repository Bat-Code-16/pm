from fastapi import APIRouter

from app.routes import managers,featuers,devicetype,device

router = APIRouter()
router.include_router(managers.router,tags=["managers"],prefix="/managers")
router.include_router(featuers.router,tags=["featuers"],prefix="/features")
router.include_router(devicetype.router,tags=["devicetype"],prefix="/devicetype")
router.include_router(device.router,tags=["device"],prefix="/device")