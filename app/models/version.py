# from sqlalchemy import Column, Integer, ForeignKey, Table, MetaData,TIMESTAMP,func

# from app.core.db import Base,engine

# metadata=MetaData()
# repo = Table('repo', metadata, autoload_with=engine)
# managers = Table('managers', metadata, autoload_with=engine)

# class Version(Base):
#     __tablename__ = "version"
    
#     id = Column(Integer, primary_key=True, index=True)
#     time = Column(TIMESTAMP(timezone=True), server_default=func.now())
#     repo_id = Column(Integer, ForeignKey(repo.c.id), nullable=False)
#     created_by = Column(Integer, ForeignKey(managers.c.id), nullable=True)
   
    
