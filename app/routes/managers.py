from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from app.database.schemas.managers import ManagerRead, ManagerCreate,ManagerLogin
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.resources import utils
from app.models.manager import Manager
from app.database.schemas.auth import Token
from app.resources.outh2 import create_access_token,OAuth2PasswordBearer



router = APIRouter()
@router.post("/create", response_model=ManagerRead)
def create_or_update_manager(manager: ManagerCreate, db: Session = Depends(get_db)):
    # Check if the manager with the provided email already exists
    existing_manager = db.query(Manager).filter(Manager.email == manager.email).first()
    
    if existing_manager:
        # Update the existing manager
        existing_manager.name = manager.name
        if manager.password:
            existing_manager.password = utils.hash(manager.password)
        existing_manager.type = manager.type
        
        db.commit()
        db.refresh(existing_manager)
        
        return existing_manager
    else:
        # Create a new Manager instance
        hashed_password = utils.hash(manager.password)
        new_manager = Manager(
            name=manager.name,
            email=manager.email,
            password=hashed_password,
            type=manager.type
        )
        
        # Add and commit the new manager to the database
        db.add(new_manager)
        db.commit()
        db.refresh(new_manager)
        
        return new_manager




@router.get("/", response_model=List[ManagerRead])
def get_managers(id: Optional[int] = Query(None), db: Session = Depends(get_db)) -> List[ManagerRead]:
    if id is None:
        # Retrieve all managers if no ID is provided
        managers = db.query(Manager).all()
    else:
        # Retrieve a specific manager if ID is provided
        manager = db.query(Manager).filter(Manager.id == id).first()
        if manager is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Manager with id {id} does not exist"
            )
        managers = [manager]
    
    return managers

@router.post("/login", response_model=Token)
def manager_login(
    manager_credentials: ManagerLogin,
    db: Session = Depends(get_db)
) -> Token:
    manager = db.query(Manager).filter(Manager.email == manager_credentials.email).first()

    if not manager:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid credentials: email not found",
        )
    
    if not utils.verify(manager_credentials.password, manager.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid credentials: incorrect password",
        )
    
    token = create_access_token({"manager_id": manager.id})
    return {"access_token": token, "token_type": "bearer"}


        
            
    
    
    

