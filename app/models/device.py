from sqlalchemy import Column, String, Boolean, Integer, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
from app.core.database import Base

class Device(Base):
    __tablename__ = 'device'

    deviceid = Column(UUID(as_uuid=True), primary_key=True)
    updated_ts = Column(Integer, nullable=False)
    # customer_id = Column(UUID(as_uuid=True), ForeignKey('customer.customerid'), nullable=False)
    additionaldetail = Column(JSONB, nullable=False)
    typeid = Column(UUID(as_uuid=True), ForeignKey('device_type.typeid', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    name = Column(String(255), nullable=False, unique=True)
    devicestateid = Column(Integer, nullable=True)
    testmodetime = Column(Integer, nullable=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    isactive = Column(Boolean, nullable=False, default=True)
    last_device_testmode_id = Column(UUID(as_uuid=True), ForeignKey('devicetestmodes.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=True)

    # Define relationships
    # customer = relationship("Customer", back_populates="device")
    device_type = relationship("DeviceType", back_populates="device")

    def __repr__(self):
        return f"<Device(deviceid={self.deviceid}, name={self.name}, typeid={self.typeid})>"
