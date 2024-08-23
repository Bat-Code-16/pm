# from sqlalchemy import Column, Integer, String,JSON,ForeignKey ,MetaData,Table
# from app.core.db import Base,engine

# metadata=MetaData()
# model = Table('model', metadata, autoload_with=engine)

# class ModelMetrics(Base):
#     __tablename__ = "model_metrics"

#     id = Column(Integer, primary_key=True, index=True)
#     model_id = Column(Integer, ForeignKey(model.c.id), nullable=False)
#     data = Column(JSON)