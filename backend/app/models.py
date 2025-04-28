from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)

class BatteryData(Base):
    __tablename__ = 'battery_data'

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    voltage = Column(Float, nullable=False)
    current = Column(Float, nullable=False)
    temperature = Column(Float, nullable=False)
    soc = Column(Float, nullable=False)  # State of Charge
    soh = Column(Float, nullable=False)  # State of Health

class LogEntry(Base):
    __tablename__ = 'log_entries'

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    level = Column(String, nullable=False)
    message = Column(String, nullable=False)

class Setting(Base):
    __tablename__ = 'settings'

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, unique=True, nullable=False)
    value = Column(String, nullable=False)
    description = Column(String, nullable=True) 