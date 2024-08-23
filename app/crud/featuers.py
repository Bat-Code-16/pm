from sqlalchemy.orm import Session
from app.models.features import Features as Model
from app.database.schemas.features import FeaturesCreate, FeaturesUpdate

def get_features(db: Session, feature_id: int):
    return db.query(Model).filter(Model.id == feature_id).first()

def create_features(db: Session, feature: FeaturesCreate):
    print(feature)
    db_feature = Model(**feature.dict())
    print(db_feature)
    db.add(db_feature)
    db.commit()
    db.refresh(db_feature)
    return db_feature

def update_features(db: Session, feature_id: int, feature: FeaturesUpdate):
    db_feature = db.query(Model).filter(Model.id == feature_id).first()
    if db_feature:
        for key, value in feature.dict().items():
            setattr(db_feature, key, value)
        db.commit()
        db.refresh(db_feature)
    return db_feature

def delete_features(db: Session, feature_id: int):
    db_feature = db.query(Model).filter(Model.id == feature_id).first()
    if db_feature:
        db.delete(db_feature)
        db.commit()
    return db_feature
