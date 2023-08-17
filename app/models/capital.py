from sqlmodel import SQLModel, Field, DateTime, Column, func
from datetime import datetime



class CapitalModel(SQLModel, table=True):
    __tablename__ = 'capital'
    id: int = Field(default=None, primary_key=True)
    name: str  = Field(max_length=100, blank=True, null=True)
    qty: int  = Field(blank=True, null=True)
    cost: float  = Field(blank=True, null=True)
    creater: str  = Field(max_length=100, blank=True, null=True)
    openid: str  = Field(max_length=255, blank=True, null=True)
    is_delete: bool = Field(default=False, blank=True, null=True)
    
    create_at: datetime = Field(default_factory=datetime.utcnow)
    update_at: datetime = Field(sa_column=Column(DateTime(), onupdate=func.now()))


    