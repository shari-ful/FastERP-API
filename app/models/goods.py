from sqlmodel import SQLModel, Field, DateTime, Column, func
from datetime import datetime



class GoodsBrandModel(SQLModel, table=True):
    __tablename__ = 'goodsbrand'
    id: int = Field(default=None, primary_key=True)
    name: str  = Field(max_length=100, blank=True, null=True)
    creater: str  = Field(max_length=100, blank=True, null=True)
    openid: str  = Field(max_length=255, blank=True, null=True)
    is_delete: bool = Field(default=False, blank=True, null=True)
    
    create_at: datetime = Field(default_factory=datetime.utcnow)
    update_at: datetime = Field(sa_column=Column(DateTime(), onupdate=func.now()))

    class Config:
        schema_extra = {
            "example": {
                "name": "Brand Name",
                "creater": "John Doe",
                "openid": "example123",
                "is_delete": False,
                "create_at": "2023-08-17T12:34:56.789Z",
                "update_at": "2023-08-17T12:34:56.789Z"
            }
        }


class GoodsClassModel(SQLModel, table=True):
    __tablename__ = 'goodsclass'
    name: str = Field(max_length=100, blank=True, null=True)
    creater: str = Field(max_length=100, blank=True, null=True)
    openid: str = Field(max_length=100, blank=True, null=True)
    is_delete: bool = Field(default=False, blank=True, null=True)
    
    create_at: datetime = Field(default_factory=datetime.utcnow)
    update_at: datetime = Field(sa_column=Column(DateTime(), onupdate=func.now()))


class GoodsColorModel(SQLModel, table=True):
    __tablename__ = 'goodscolor'
    name: str = Field(max_length=100, blank=True, null=True)
    creater: str = Field(max_length=100, blank=True, null=True)
    openid: str = Field(max_length=100, blank=True, null=True)
    is_delete: bool = Field(default=False, blank=True, null=True)
    
    create_at: datetime = Field(default_factory=datetime.utcnow)
    update_at: datetime = Field(sa_column=Column(DateTime(), onupdate=func.now()))

class GoodsOriginModel(SQLModel, table=True):
    __tablename__ = 'goodsorigin'
    name: str = Field(max_length=100, blank=True, null=True)
    creater: str = Field(max_length=100, blank=True, null=True)
    openid: str = Field(max_length=100, blank=True, null=True)
    is_delete: bool = Field(default=False, blank=True, null=True)
    
    create_at: datetime = Field(default_factory=datetime.utcnow)
    update_at: datetime = Field(sa_column=Column(DateTime(), onupdate=func.now()))

class GoodsShapeModel(SQLModel, table=True):
    __tablename__ = 'goodsshape'
    name: str = Field(max_length=100, blank=True, null=True)
    creater: str = Field(max_length=100, blank=True, null=True)
    openid: str = Field(max_length=100, blank=True, null=True)
    is_delete: bool = Field(default=False, blank=True, null=True)
    
    create_at: datetime = Field(default_factory=datetime.utcnow)
    update_at: datetime = Field(sa_column=Column(DateTime(), onupdate=func.now()))

class GoodsSpecsModel(SQLModel, table=True):
    __tablename__ = 'goodspecs'
    name: str = Field(max_length=100, blank=True, null=True)
    creater: str = Field(max_length=100, blank=True, null=True)
    openid: str = Field(max_length=100, blank=True, null=True)
    is_delete: bool = Field(default=False, blank=True, null=True)
    
    create_at: datetime = Field(default_factory=datetime.utcnow)
    update_at: datetime = Field(sa_column=Column(DateTime(), onupdate=func.now()))


class GoodsUnitModel(SQLModel, table=True):
    __tablename__ = 'goodsunit'
    name: str = Field(max_length=100, blank=True, null=True)
    creater: str = Field(max_length=100, blank=True, null=True)
    openid: str = Field(max_length=100, blank=True, null=True)
    is_delete: bool = Field(default=False, blank=True, null=True)
    
    create_at: datetime = Field(default_factory=datetime.utcnow)
    update_at: datetime = Field(sa_column=Column(DateTime(), onupdate=func.now()))

class GoodsModel(SQLModel, table=True):
    __tablename__ = 'goods'
    id: int = Field(default=None, primary_key=True)
    goods_code: str = Field(max_length=50, blank=True, null=True)
    goods_desc: str  = Field(max_length=255, blank=True, null=True)
    goods_supplier: str  = Field(max_length=100, blank=True, null=True)
    goods_weight: float = Field(default=0, blank=True, null=True)
    goods_w: float = Field(default=0, blank=True, null=True)
    goods_d: float = Field(default=0, blank=True, null=True)
    goods_h: float = Field(default=0, blank=True, null=True)
    unit_volume: float = Field(default=0, blank=True, null=True)
    goods_unit: str  = Field(max_length=100, blank=True, null=True)
    goods_class: str  = Field(max_length=100, blank=True, null=True)
    goods_brand: str  = Field(max_length=100, blank=True, null=True)
    goods_color: str  = Field(max_length=50,blank=True, null=True)
    goods_shape: str  = Field(max_length=50, blank=True, null=True)
    goods_specs: str  = Field(max_length=50, blank=True, null=True)
    goods_origin: str  = Field(max_length=50, blank=True, null=True)
    safety_stock: int = Field(default=0, blank=True, null=True)
    goods_cost = Field(default=0, blank=True, null=True)
    goods_price = Field(default=0, blank=True, null=True)
    creater: str  = Field(max_length=150, blank=True, null=True)
    bar_code: str  = Field(max_length=100, blank=True, null=True)
    openid: str  = Field(max_length=100, blank=True, null=True)
    is_delete: bool = Field(default=False, blank=True, null=True)

    create_at: datetime = Field(default_factory=datetime.utcnow)
    update_at: datetime = Field(sa_column=Column(DateTime(), onupdate=func.now()))


