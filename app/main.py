from fastapi import FastAPI
from . import models
from app.core.database import engine
from app.routes.api import router 
from app.core.config import settings
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings



app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router,prefix=settings.api_prefix)



@app.get("/")
def root():
    return {"message": "Welcome to my API"}
