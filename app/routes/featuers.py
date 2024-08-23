from fastapi import APIRouter, FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal, engine
import app.models.features as models
import app.crud.featuers as crud
import app.database.schemas.features as schemas
from app.core.database import get_db

router = APIRouter()
# Create the database tables if not exist
models.Base.metadata.create_all(bind=engine)



@router.post("/features/", response_model=schemas.Features)
def create_feature(feature: schemas.FeaturesCreate, db: Session = Depends(get_db)):
    return crud.create_features(db, feature)

@router.get("/features/{feature_id}", response_model=schemas.Features)
def read_feature(feature_id: int, db: Session = Depends(get_db)):
    db_feature = crud.get_features(db, feature_id)
    if db_feature is None:
        raise HTTPException(status_code=404, detail="Feature not found")
    return db_feature

@router.put("/features/{feature_id}", response_model=schemas.Features)
def update_feature(feature_id: int, feature: schemas.FeaturesUpdate, db: Session = Depends(get_db)):
    db_feature = crud.update_features(db, feature_id, feature)
    if db_feature is None:
        raise HTTPException(status_code=404, detail="Feature not found")
    return db_feature

@router.delete("/features/{feature_id}", response_model=schemas.Features)
def delete_feature(feature_id: int, db: Session = Depends(get_db)):
    db_feature = crud.delete_features(db, feature_id)
    if db_feature is None:
        raise HTTPException(status_code=404, detail="Feature not found")
    return db_feature
