from fastapi import APIRouter, Depends, status
from sqlmodel import Session, select

from ..database import get_session
from ..models import PantryItem, PantryItemCreate, PantryItemRead

router = APIRouter(prefix="/pantry-items", tags=["pantry-items"])


@router.get("", response_model=list[PantryItemRead])
def list_pantry_items(session: Session = Depends(get_session)):
    return session.exec(select(PantryItem)).all()


@router.post("", response_model=PantryItemRead, status_code=status.HTTP_201_CREATED)
def create_pantry_item(payload: PantryItemCreate, session: Session = Depends(get_session)):
    obj = PantryItem(**payload.model_dump())
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj
