from sqlmodel import SQLModel, Field, DateTime, Column, func
from datetime import datetime



class CompanyModel(SQLModel, table=True):
    __tablename__ = 'company'
    id: int = Field(default=None, primary_key=True)
    name: str  = Field(max_length=100, blank=True, null=True)
    city: str  = Field(max_length=100, blank=True, null=True)
    address: str  = Field(max_length=100, blank=True, null=True)
    contact: str  = Field(max_length=100, blank=True, null=True)
    manager: str  = Field(max_length=100, blank=True, null=True)
    creater: str  = Field(max_length=100, blank=True, null=True)
    openid: str  = Field(max_length=255, blank=True, null=True)
    is_delete: bool = Field(default=False, blank=True, null=True)
    
    create_at: datetime = Field(default_factory=datetime.utcnow)
    update_at: datetime = Field(sa_column=Column(DateTime(), onupdate=func.now()))

    