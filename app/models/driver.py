from sqlmodel import SQLModel, Field, DateTime, Column, func
from datetime import datetime

class DriverModel(SQLModel, table=True):
    __tablename__ = 'driver'
    name: str  = Field(max_length=255, blank=True, null=True)
    license_plate: str  = Field(max_length=255, blank=True, null=True)
    contact: str  = Field(max_length=255, blank=True, null=True)
    creater: str  = Field(max_length=100, blank=True, null=True)
    openid: str  = Field(max_length=255, blank=True, null=True)
    is_delete: bool = Field(default=False, blank=True, null=True)
    
    create_at: datetime = Field(default_factory=datetime.utcnow)
    update_at: datetime = Field(sa_column=Column(DateTime(), onupdate=func.now()))


class DispatchModel(SQLModel, table=True):
    __tablename__ = 'dispatch'
    driver_name: str  = Field(max_length=255, blank=True, null=True)
    dn_code: str  = Field(max_length=255, blank=True, null=True)
    contact: int = Field(default=None, primary_key=True)
    creater: str  = Field(max_length=100, blank=True, null=True)
    openid: str  = Field(max_length=255, blank=True, null=True)
    is_delete: bool = Field(default=False, blank=True, null=True)
    
    create_at: datetime = Field(default_factory=datetime.utcnow)
    update_at: datetime = Field(sa_column=Column(DateTime(), onupdate=func.now()))
