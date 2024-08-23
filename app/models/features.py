from sqlalchemy import Column,  Integer, String, ForeignKey, ARRAY, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from sqlalchemy.orm import relationship
from app.core.database import Base,engine
from app.models.devicetype import DeviceType

metadata = MetaData()



class Features(Base):
    __tablename__ = 'features'

    id = Column(Integer, primary_key=True, index=True)
    device_type_id = Column(UUID(as_uuid=True), ForeignKey('device_type.typeid', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    names = Column(ARRAY(String), nullable=False)
    alias = Column(ARRAY(String), nullable=True)
    valid_ranges = Column(ARRAY(String), nullable=True)

    # Define relationships
    device_type = relationship("DeviceType", back_populates="features")


    def __repr__(self):
        return f"<Features(id={self.id}, device_type_id={self.device_type_id}, names={self.names})>"