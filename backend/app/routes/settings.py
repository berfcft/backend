from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter()

# Add a new setting
@router.post("/", response_model=schemas.SettingResponse)
def add_setting(setting: schemas.SettingCreate, db: Session = Depends(get_db)):
    return crud.create_setting(db=db, setting=setting)

# Update an existing setting
@router.put("/{setting_id}", response_model=schemas.SettingResponse)
def update_setting(setting_id: int, setting: schemas.SettingUpdate, db: Session = Depends(get_db)):
    db_setting = crud.update_setting(db=db, setting_id=setting_id, setting=setting)
    if db_setting is None:
        raise HTTPException(status_code=404, detail="Setting not found")
    return db_setting

# Get a setting by key
@router.get("/key/{key}", response_model=schemas.SettingResponse)
def get_setting_by_key(key: str, db: Session = Depends(get_db)):
    db_setting = crud.get_setting_by_key(db=db, key=key)
    if db_setting is None:
        raise HTTPException(status_code=404, detail="Setting not found")
    return db_setting

# Get all settings
@router.get("/", response_model=list[schemas.SettingResponse])
def get_all_settings(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_all_settings(db=db, skip=skip, limit=limit) 