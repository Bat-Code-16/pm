from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.core.database import Base
from sqlalchemy.orm import Session

class DeviceType(Base):
    __tablename__ = 'device_type'

    typeid = Column(UUID(as_uuid=True), primary_key=True)
    type = Column(String, nullable=False, unique=True)
    label = Column(String, nullable=False, unique=True)

    # Define relationships
    features = relationship("Features", back_populates="device_type")
    device=relationship("Device",back_populates="device_type")

    def __repr__(self):
        return f"<DeviceType(typeid={self.typeid}, type={self.type}, label={self.label})>"
    
    @classmethod
    def get_all(cls, db: Session):
        return db.query(cls).all()