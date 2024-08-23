from sqlalchemy import Column, String, Boolean, JSON, BigInteger, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customer'

    customerid = Column(UUID(as_uuid=True), primary_key=True)
    customertitle = Column(String(255), nullable=True)
    usewebsocket = Column(Boolean, nullable=True)
    stncode = Column(String(10), nullable=False, unique=True)
    zonecode = Column(String(10), nullable=False)
    divisioncode = Column(String(10), nullable=False)
    additionaldetail = Column(JSON, nullable=True)
    updated_ts = Column(BigInteger, nullable=False)

    # Define relationship to Device
    devices = relationship("Device", back_populates="customer")

    __table_args__ = (
        UniqueConstraint('stncode', 'zonecode', 'divisioncode', name='customer_un'),
    )
