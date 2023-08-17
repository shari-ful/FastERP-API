from pydantic import BaseModel
from datetime import datetime

class CreateGoodsBrand(BaseModel):
    name: str
    creater: str
    openid: str

class UpdateGoodsBrand(BaseModel):
    name: str
    creater: str
    openid: str
    is_delete: bool

class BaseGoodsBrand(CreateGoodsBrand):
    id: int
    create_time: datetime
    update_time: datetime

class GoodsBrand(BaseGoodsBrand):
    class Config:
        orm_mode = True