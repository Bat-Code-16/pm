# from sqlalchemy import Column, Integer, ForeignKey, Table, MetaData, JSON, UUID
# from app.core.db import Base, engine

# metadata = MetaData()

# # Reflecting tables
# features = Table('features', metadata, autoload_with=engine)
# device_type = Table('device_type', metadata, autoload_with=engine)
# model_type = Table('model_type', metadata, autoload_with=engine)


# class AnomaliesTemplate(Base):
#     __tablename__ = "anomalies_template"
    
#     id = Column(Integer, primary_key=True, index=True)
#     feature_id = Column(Integer, ForeignKey(features.c.id), nullable=False)
#     model_type_id = Column(Integer, ForeignKey(model_type.c.id), nullable=False)
#     device_type_id = Column(UUID(as_uuid=True), ForeignKey(device_type.c.typeid), nullable=False)
    
#     template_data=-Column(JSON)
  