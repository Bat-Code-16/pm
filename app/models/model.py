
# from sqlalchemy import Column, Integer, ForeignKey, Table, MetaData, JSON,Boolean
# from app.core.db import Base, engine

# metadata = MetaData()

# # Reflecting tables
# features = Table('features', metadata, autoload_with=engine)
# model_type = Table('model_type', metadata, autoload_with=engine)
# anomalies = Table('anomalies_template', metadata, autoload_with=engine)
# version = Table('version', metadata, autoload_with=engine)
# scaler = Table('scaler', metadata, autoload_with=engine)
# repo = Table('repo', metadata, autoload_with=engine)

# class Model(Base):
#     __tablename__ = "model"
    
#     id = Column(Integer, primary_key=True, index=True)
#     version_id = Column(Integer, ForeignKey(version.c.id), nullable=False)
#     enable=Column(Boolean)
#     feature_id = Column(Integer, ForeignKey(features.c.id), nullable=False)
#     model_type_id = Column(Integer, ForeignKey(model_type.c.id), nullable=False)
#     anomalies_id = Column(Integer, ForeignKey(anomalies.c.id), nullable=False)
#     scaler_id = Column(Integer, ForeignKey(scaler.c.id), nullable=False)
#     repo_id = Column(Integer, ForeignKey(repo.c.id), nullable=False)
#     data=-Column(JSON)