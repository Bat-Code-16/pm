from sqlalchemy import Column, Integer, String,JSON
from app.core.db import Base

class ModelType(Base):
    __tablename__ = "model_type"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)
    hyperparameter = Column(JSON)
