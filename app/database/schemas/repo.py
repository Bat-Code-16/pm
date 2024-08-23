from pydantic import BaseModel

class RepoBase(BaseModel):
    path: str

class RepoCreate(RepoBase):
    pass

class RepoUpdate(BaseModel):
    path: str

class Repo(RepoBase):
    id: int

    class Config:
        orm_mode = True
