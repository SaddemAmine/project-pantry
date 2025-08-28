from fastapi import APIRouter, Depends, status
from sqlmodel import Session, select

from ..database import get_session
from ..models import RecipeItem, RecipeItemCreate, RecipeItemRead

router = APIRouter(prefix="/recipe-items", tags=["recipe-items"])


@router.get("", response_model=list[RecipeItemRead])
def list_recipe_items(session: Session = Depends(get_session)):
    return session.exec(select(RecipeItem)).all()


@router.post("", response_model=RecipeItemRead, status_code=status.HTTP_201_CREATED)
def create_recipe_item(payload: RecipeItemCreate, session: Session = Depends(get_session)):
    obj = RecipeItem(**payload.model_dump())
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj
