from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Repo(Base):
    __tablename__ = 'repo'

    id = Column(Integer, primary_key=True, index=True)
    path = Column(String, nullable=False)

    def __repr__(self):
        return f"<Repo(id={self.id}, path={self.path})>"
