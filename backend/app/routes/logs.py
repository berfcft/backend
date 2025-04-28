from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter()

# Add a new log entry
@router.post("/", response_model=schemas.LogEntryResponse)
def add_log_entry(log_entry: schemas.LogEntryCreate, db: Session = Depends(get_db)):
    return crud.create_log_entry(db=db, log_entry=log_entry)

# Get all log entries
@router.get("/", response_model=list[schemas.LogEntryResponse])
def get_log_entries(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_log_entries(db=db, skip=skip, limit=limit) 