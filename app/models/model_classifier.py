
# from sqlalchemy import Column, Integer, ForeignKey, Table, MetaData, JSON,Float,Enum
# from app.core.db import Base, engine
# import enum
# metadata = MetaData()

# # Reflecting tables
# class ModelType(enum.Enum):
#     good = "good"
#     bad = "bad"
#     unknown = "unknown"

# anomalies = Table('anomalies_template', metadata, autoload_with=engine)
# model = Table('model', metadata, autoload_with=engine)



# class ModelClassifier(Base):
#     __tablename__ = "modelClassifier"
    
#     id = Column(Integer, primary_key=True, index=True)
#     passed = Column(Integer)
#     anomalies_id = Column(Integer, ForeignKey(anomalies.c.id), nullable=False)
#     model_id = Column(Integer, ForeignKey(model.c.id), nullable=False)
#     population_fraction=Column(Float)
#     additional_details=-Column(JSON)
#     model_type=Column(Enum(ModelType),nullable=False)