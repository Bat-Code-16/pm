# from sqlalchemy import Column, Integer, ForeignKey, Table, MetaData

# from app.core.db import Base,engine

# metadata=MetaData()
# repo = Table('repo', metadata, autoload_with=engine)
# featuers = Table('features', metadata, autoload_with=engine)
# version = Table('version', metadata, autoload_with=engine)

# class Scaler(Base):
#     __tablename__ = "scaler"
    
#     id = Column(Integer, primary_key=True, index=True)
#     feature_id = Column(Integer, ForeignKey(featuers.c.id), nullable=False)
#     repo_id = Column(Integer, ForeignKey(repo.c.id), nullable=False)
#     version_id = Column(Integer, ForeignKey(version.c.id), nullable=False)
   