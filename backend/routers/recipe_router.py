from fastapi import APIRouter, Depends, status
from sqlmodel import Session, select

from ..database import get_session
from ..models import Recipe, RecipeCreate, RecipeRead

router = APIRouter(prefix="/recipes", tags=["recipes"])


@router.get("", response_model=list[RecipeRead])
def list_recipes(session: Session = Depends(get_session)):
    return session.exec(select(Recipe)).all()


@router.post("", response_model=RecipeRead, status_code=status.HTTP_201_CREATED)
def create_recipe(payload: RecipeCreate, session: Session = Depends(get_session)):
    obj = Recipe(**payload.model_dump())
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj
