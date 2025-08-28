from fastapi import APIRouter, Depends, status
from sqlmodel import Session, select

from ..database import get_session
from ..models import (
    RecipeInstruction,
    RecipeInstructionCreate,
    RecipeInstructionRead,
)

router = APIRouter(prefix="/recipe-instructions", tags=["recipe-instructions"])


@router.get("", response_model=list[RecipeInstructionRead])
def list_recipe_instructions(session: Session = Depends(get_session)):
    return session.exec(select(RecipeInstruction)).all()


@router.post("", response_model=RecipeInstructionRead, status_code=status.HTTP_201_CREATED)
def create_recipe_instruction(
    payload: RecipeInstructionCreate, session: Session = Depends(get_session)
):
    obj = RecipeInstruction(**payload.model_dump())
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj
