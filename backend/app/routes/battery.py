from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter()

# Add new battery data
@router.post("/", response_model=schemas.BatteryDataResponse)
def add_battery_data(battery_data: schemas.BatteryDataCreate, db: Session = Depends(get_db)):
    return crud.create_battery_data(db=db, battery_data=battery_data)

# Get the latest battery data
@router.get("/", response_model=schemas.BatteryDataResponse)
def get_latest_battery_data(db: Session = Depends(get_db)):
    battery_data = crud.get_latest_battery_data(db=db)
    if battery_data is None:
        raise HTTPException(status_code=404, detail="No battery data found")
    return battery_data 