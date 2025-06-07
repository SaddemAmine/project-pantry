from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ..models import Item
from ..schemas import Item as ItemSchema
from ..database import get_db


router = APIRouter()


@router.get("/items")
async def get_items():
    return {"message": "List of items"}


@router.post(
    "/items",
    response_model=ItemSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_item(item: Item, db: Session = Depends(get_db)):
    pass
