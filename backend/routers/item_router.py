from fastapi import APIRouter, Depends, status
from sqlmodel import Session, select

from ..models.item import Item, ItemCreate, ItemRead
from ..database import get_session

router = APIRouter(tags=["items"])


@router.get("/items", response_model=list[ItemRead])
def list_items(session: Session = Depends(get_session)):
    return session.exec(select(Item)).all()


@router.post("/items", response_model=ItemRead, status_code=status.HTTP_201_CREATED)
def create_item(payload: ItemCreate, session: Session = Depends(get_session)):
    item = Item(**payload.model_dump())
    session.add(item)
    session.commit()
    session.refresh(item)
    return item
