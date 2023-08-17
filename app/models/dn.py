from sqlmodel import SQLModel, Field, DateTime, Column, func
from datetime import datetime



class DnListModel(SQLModel, table=True):
    __tablename__ = 'dnlist'
    id: int = Field(default=None, primary_key=True)
    dn_code: str  = Field(max_length=255, blank=True, null=True)
    dn_status: int  = Field(blank=True, null=True)
    total_weight: float  = Field(blank=True, null=True)
    total_volume: float  = Field(blank=True, null=True)
    total_cost: float  = Field(blank=True, null=True)
    customer: str  = Field(max_length=255, blank=True, null=True)
    bar_code: str  = Field(max_length=255, blank=True, null=True)
    back_order_label: bool = Field(default=False, blank=True, null=True)
    creater: str  = Field(max_length=100, blank=True, null=True)
    openid: str  = Field(max_length=255, blank=True, null=True)
    is_delete: bool = Field(default=False, blank=True, null=True)
    
    create_at: datetime = Field(default_factory=datetime.utcnow)
    update_at: datetime = Field(sa_column=Column(DateTime(), onupdate=func.now()))



class DnDetailModel(SQLModel, table=True):
    __tablename__ = 'dndetail'
    dn_code: str  = Field(max_length=255, blank=True, null=True)
    dn_status: int  = Field(blank=True, null=True)
    customer: str  = Field(max_length=255, blank=True, null=True)
    goods_code: str  = Field(max_length=255, blank=True, null=True)
    goods_desc: str  = Field(max_length=255, blank=True, null=True)
    goods_qty: int  = Field(blank=True, null=True)
    pick_qty: int  = Field(blank=True, null=True)
    picked_qty: int  = Field(blank=True, null=True)
    intransit_qty: int  = Field(blank=True, null=True)
    delivery_actual_qty: int  = Field(blank=True, null=True)
    delivery_shortage_qty: int  = Field(blank=True, null=True)
    delivery_more_qty: int  = Field(blank=True, null=True)
    delivery_damage_qty: int  = Field(blank=True, null=True)
    goods_weight: float  = Field(blank=True, null=True)
    goods_volume: float  = Field(blank=True, null=True)
    goods_cost: float  = Field(blank=True, null=True)
    creater: str  = Field(max_length=100, blank=True, null=True)
    back_order_label: bool = Field(default=False, blank=True, null=True)
    creater: str  = Field(max_length=100, blank=True, null=True)
    openid: str  = Field(max_length=255, blank=True, null=True)
    is_delete: bool = Field(default=False, blank=True, null=True)
    
    create_at: datetime = Field(default_factory=datetime.utcnow)
    update_at: datetime = Field(sa_column=Column(DateTime(), onupdate=func.now()))


class DnPickingModel(SQLModel, table=True):
    __tablename__ = 'pickinglist'
    dn_code: str  = Field(max_length=100, blank=True, null=True)
    bin_name: str  = Field(max_length=100, blank=True, null=True)
    goods_code: str  = Field(max_length=100, blank=True, null=True)
    picking_status: int  = Field(blank=True, null=True)
    pick_qty: int  = Field(blank=True, null=True)
    picked_qty: int  = Field(blank=True, null=True)
    creater: str  = Field(max_length=100, blank=True, null=True)
    t_code: str  = Field(max_length=100, blank=True, null=True)
    openid: str  = Field(max_length=100, blank=True, null=True)

    create_at: datetime = Field(default_factory=datetime.utcnow)
    update_at: datetime = Field(sa_column=Column(DateTime(), onupdate=func.now()))
