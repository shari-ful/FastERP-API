from sqlmodel import SQLModel, Field, DateTime
from datetime import datetime

class GoodsModel(SQLModel, table=True):
    __tablename__ = 'goods'
    id: int = Field(default=None, primary_key=True)
    goods_code: str = Field(max_length=50, verbose_name="Goods Code")
    goods_desc: str  = Field(max_length=255, verbose_name="Goods Description")
    goods_supplier: str  = Field(max_length=100, verbose_name="Goods Supplier")
    goods_weight: float = Field(default=0, verbose_name="Goods Weight")
    goods_w: float = Field(default=0, verbose_name="Goods Width")
    goods_d: float = Field(default=0, verbose_name="Goods Depth")
    goods_h: float = Field(default=0, verbose_name="Goods Height")
    unit_volume: float = Field(default=0, verbose_name="Unit Volume")
    goods_unit: str  = Field(max_length=100, verbose_name="Goods Unit")
    goods_class: str  = Field(max_length=100, verbose_name="Goods Class")
    goods_brand: str  = Field(max_length=100, verbose_name="Goods Brand")
    goods_color: str  = Field(max_length=50, verbose_name="Goods Color")
    goods_shape: str  = Field(max_length=50, verbose_name="Goods Shape")
    goods_specs: str  = Field(max_length=50, verbose_name="Goods Specs")
    goods_origin: str  = Field(max_length=50, verbose_name="Goods Origin")
    safety_stock: int = Field(default=0, verbose_name="Goods Safety Stock")
    goods_cost = Field(default=0, verbose_name="Goods Cost")
    goods_price = Field(default=0, verbose_name="Goods Price")
    creater: str  = Field(max_length=150, verbose_name="Who created")
    bar_code: str  = Field(max_length=100, verbose_name="Bar Code")
    openid: str  = Field(max_length=100, verbose_name="Openid")
    is_delete: bool = Field(default=False, verbose_name='Delete Label')

    create_time: DateTime = Field(auto_now_add=True, verbose_name="Create Time")
    update_time: DateTime = Field(auto_now=True, blank=True, null=True, verbose_name="Update Time")