from sqlmodel import SQLModel, Field, DateTime, Column, func
from datetime import datetime


class AsnModel(SQLModel, table=True):
    __tablename__ = 'asn'
    asn_code: str = Field(max_length=100, blank=True, null=True)
    asn_status: int= Field(default=1, blank=True, null=True)
    total_weight: int= Field(default=0, blank=True, null=True)
    total_volume: int= Field(default=0, blank=True, null=True)
    total_cost: int= Field(default=0, blank=True, null=True)
    supplier: str = Field(max_length=100, blank=True, null=True)
    creater: str = Field(max_length=100, blank=True, null=True)
    bar_code: str = Field(max_length=100, blank=True, null=True)
    openid: str = Field(max_length=100, blank=True, null=True)
    transportation_fee: dict = Field(default=dict, blank=True, null=True)
    is_delete: bool = Field(default=False, blank=True, null=True)

    create_at: datetime = Field(default_factory=datetime.utcnow)
    update_at: datetime = Field(sa_column=Column(DateTime(), onupdate=func.now()))

        

class AsnDetailModel(SQLModel, table=True):
    __tablename__ = 'asndetails'
    asn_code: str = Field(max_length=100, blank=True, null=True)
    asn_status: int= Field(default=1, blank=True, null=True)
    supplier: str = Field(max_length=100, blank=True, null=True)
    goods_code: str = Field(max_length=100, blank=True, null=True)
    goods_desc: str = Field(max_length=100, blank=True, null=True)
    goods_qty: int= Field(default=0, blank=True, null=True)
    goods_actual_qty: int= Field(default=0, blank=True, null=True)
    sorted_qty: int= Field(default=0, blank=True, null=True)
    goods_shortage_qty: int= Field(default=0, blank=True, null=True)
    goods_more_qty: int= Field(default=0, blank=True, null=True)
    goods_damage_qty: int= Field(default=0, blank=True, null=True)
    goods_weight: int= Field(default=0, blank=True, null=True)
    goods_volume: int= Field(default=0, blank=True, null=True)
    goods_cost: int= Field(default=0, blank=True, null=True)
    creater: str = Field(max_length=100, blank=True, null=True)
    openid: str = Field(max_length=100, blank=True, null=True)
    is_delete: bool = Field(default=False, blank=True, null=True)
    
    create_at: datetime = Field(default_factory=datetime.utcnow)
    update_at: datetime = Field(sa_column=Column(DateTime(), onupdate=func.now()))
