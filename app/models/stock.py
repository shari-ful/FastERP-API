from sqlmodel import SQLModel, Field, DateTime, Column, func
from datetime import datetime

class StockModel(SQLModel, table=True):
    __tablename__ = 'stock'
    goods_code: str = Field(max_length=100, blank=True, null=True)
    goods_desc: str = Field(max_length=100, blank=True, null=True)
    goods_qty: int = Field(default=0, blank=True, null=True)
    onhand_stock: int = Field(default=0, blank=True, null=True)
    can_order_stock: int = Field(default=0, blank=True, null=True)
    ordered_stock: int = Field(default=0, blank=True, null=True)
    inspect_stock: int = Field(default=0, blank=True, null=True)
    hold_stock: int = Field(default=0, blank=True, null=True)
    damage_stock: int = Field(default=0, blank=True, null=True)
    asn_stock: int = Field(default=0, blank=True, null=True)
    dn_stock: int = Field(default=0, blank=True, null=True)
    pre_load_stock: int = Field(default=0, blank=True, null=True)
    pre_sort_stock: int = Field(default=0, blank=True, null=True)
    sorted_stock: int = Field(default=0,blank=True, null=True)
    pick_stock: int = Field(default=0, blank=True, null=True)
    picked_stock: int = Field(default=0, blank=True, null=True)
    back_order_stock: int = Field(default=0, blank=True, null=True)
    supplier: str = Field(default='', max_length=255, blank=True, null=True)
    openid: str = Field(max_length=100, blank=True, null=True)
    
    create_at: datetime = Field(default_factory=datetime.utcnow)
    update_at: datetime = Field(sa_column=Column(DateTime(), onupdate=func.now()))


class StockBinModel(SQLModel, table=True):
    __tablename__ = 'stockbin'
    bin_name: str = Field(max_length=100, blank=True, null=True)
    goods_code: str = Field(max_length=100, blank=True, null=True)
    goods_desc: str = Field(max_length=100, blank=True, null=True)
    goods_qty: int = Field(default=0, blank=True, null=True)
    pick_qty: int = Field(default=0, blank=True, null=True)
    picked_qty: int = Field(default=0, blank=True, null=True)
    bin_size: str = Field(max_length=100, blank=True, null=True)
    bin_property: str = Field(max_length=100, blank=True, null=True)
    t_code: str = Field(max_length=100, blank=True, null=True)
    openid: str = Field(max_length=100, blank=True, null=True)
    
    create_at: datetime = Field(default_factory=datetime.utcnow)
    update_at: datetime = Field(sa_column=Column(DateTime(), onupdate=func.now()))
