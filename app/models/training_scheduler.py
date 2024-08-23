# from sqlalchemy import Column, Integer, ForeignKey, Table, MetaData, ARRAY, String, UUID,Enum
# from app.core.db import Base, engine
# import enum
# metadata = MetaData()
# class TimeType(enum.Enum):
#     latest="latest"
#     old="old"
    
# # Reflecting tables
# features = Table('features', metadata, autoload_with=engine)
# model_type = Table('model_type', metadata, autoload_with=engine)
# device_type = Table('device_type', metadata, autoload_with=engine)


# class TrainingScheduler(Base):
#     __tablename__ = "training_scheduler"
    
#     id = Column(Integer, primary_key=True, index=True)
#     feature_id = Column(Integer, ForeignKey(features.c.id), nullable=False)
#     model_type_id = Column(Integer, ForeignKey(model_type.c.id), nullable=False)
#     device_type_id = Column(UUID(as_uuid=True), ForeignKey(device_type.c.typeid), nullable=False)
#     time_period_hour = Column(Integer, nullable=False)
#     cron_expression = Column(ARRAY(String), nullable=False)
#     typetime=Column(Enum(TimeType),nullable=False)



   