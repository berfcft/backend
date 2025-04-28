from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserLogin(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    is_admin: bool

    model_config = {
        "from_attributes": True
    }

class BatteryDataBase(BaseModel):
    voltage: float
    current: float
    temperature: float
    soc: float  # State of Charge
    soh: float  # State of Health

class BatteryDataCreate(BatteryDataBase):
    pass

class BatteryDataResponse(BatteryDataBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True

class LogEntryBase(BaseModel):
    level: str
    message: str

class LogEntryCreate(LogEntryBase):
    pass

class LogEntryResponse(LogEntryBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True

class SettingBase(BaseModel):
    key: str
    value: str
    description: Optional[str] = None

class SettingCreate(SettingBase):
    pass

class SettingUpdate(BaseModel):
    value: Optional[str] = None
    description: Optional[str] = None

class SettingResponse(SettingBase):
    id: int

    class Config:
        orm_mode = True
