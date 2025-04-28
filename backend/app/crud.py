from sqlalchemy.orm import Session
from app import models, schemas
from typing import Optional

# Create a new user
def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get a user by email
def get_user_by_email(db: Session, email: str) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.email == email).first()

# Add new battery data
def create_battery_data(db: Session, battery_data: schemas.BatteryDataCreate) -> models.BatteryData:
    db_battery_data = models.BatteryData(**battery_data.dict())
    db.add(db_battery_data)
    db.commit()
    db.refresh(db_battery_data)
    return db_battery_data

# Get the latest battery data
def get_latest_battery_data(db: Session) -> Optional[models.BatteryData]:
    return db.query(models.BatteryData).order_by(models.BatteryData.timestamp.desc()).first()

# Add a new log entry
def create_log_entry(db: Session, log_entry: schemas.LogEntryCreate) -> models.LogEntry:
    db_log_entry = models.LogEntry(**log_entry.dict())
    db.add(db_log_entry)
    db.commit()
    db.refresh(db_log_entry)
    return db_log_entry

# Get all log entries
def get_log_entries(db: Session, skip: int = 0, limit: int = 10) -> list[models.LogEntry]:
    return db.query(models.LogEntry).offset(skip).limit(limit).all()

# Add a new setting
def create_setting(db: Session, setting: schemas.SettingCreate) -> models.Setting:
    db_setting = models.Setting(**setting.dict())
    db.add(db_setting)
    db.commit()
    db.refresh(db_setting)
    return db_setting

# Update an existing setting
def update_setting(db: Session, setting_id: int, setting: schemas.SettingUpdate) -> Optional[models.Setting]:
    db_setting = db.query(models.Setting).filter(models.Setting.id == setting_id).first()
    if db_setting is None:
        return None
    for key, value in setting.dict(exclude_unset=True).items():
        setattr(db_setting, key, value)
    db.commit()
    db.refresh(db_setting)
    return db_setting

# Get a setting by key
def get_setting_by_key(db: Session, key: str) -> Optional[models.Setting]:
    return db.query(models.Setting).filter(models.Setting.key == key).first()

# Get all settings
def get_all_settings(db: Session, skip: int = 0, limit: int = 10) -> list[models.Setting]:
    return db.query(models.Setting).offset(skip).limit(limit).all() 