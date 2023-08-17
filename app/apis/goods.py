from fastapi import APIRouter

api = APIRouter()

@api.get('/')
async def get_goods():
    pass