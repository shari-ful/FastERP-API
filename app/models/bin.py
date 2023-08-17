from sqlmodel import SQLModel, Field, DateTime, Column, func
from datetime import datetime



class BinPropertyModel(SQLModel, table=True):
    __tablename__ = 'binproperty'
    id: int = Field(default=None, primary_key=True)
    name: str  = Field(max_length=100, blank=True, null=True)
    creater: str  = Field(max_length=100, blank=True, null=True)
    openid: str  = Field(max_length=255, blank=True, null=True)
    is_delete: bool = Field(default=False, blank=True, null=True)
    
    create_at: datetime = Field(default_factory=datetime.utcnow)
    update_at: datetime = Field(sa_column=Column(DateTime(), onupdate=func.now()))


class BinSetModel(SQLModel, table=True):
    __tablename__ = 'binset'
    id: int = Field(default=None, primary_key=True)
    name: str  = Field(max_length=100, blank=True, null=True)
    bin_size: str  = Field(max_length=100, blank=True, null=True)
    bin_property: str  = Field(max_length=100, blank=True, null=True)
    empty_label: str  = Field(max_length=100, blank=True, null=True)
    bar_code: str  = Field(max_length=100, blank=True, null=True)
    creater: str  = Field(max_length=100, blank=True, null=True)
    openid: str  = Field(max_length=255, blank=True, null=True)
    is_delete: bool = Field(default=False, blank=True, null=True)
    
    create_at: datetime = Field(default_factory=datetime.utcnow)
    update_at: datetime = Field(sa_column=Column(DateTime(), onupdate=func.now()))

class BinSizeModel(SQLModel, table=True):
    __tablename__ = 'binsize'
    id: int = Field(default=None, primary_key=True)
    bin_size: str  = Field(max_length=100, blank=True, null=True)
    bin_size: str  = Field(max_length=100, blank=True, null=True)
    bin_size_w: float  = Field(blank=True, null=True)
    bin_size_d: float  = Field(blank=True, null=True)
    bin_size_h: float  = Field(blank=True, null=True)
    creater: str  = Field(max_length=100, blank=True, null=True)
    openid: str  = Field(max_length=255, blank=True, null=True)
    is_delete: bool = Field(default=False, blank=True, null=True)
    
    create_at: datetime = Field(default_factory=datetime.utcnow)
    update_at: datetime = Field(sa_column=Column(DateTime(), onupdate=func.now()))