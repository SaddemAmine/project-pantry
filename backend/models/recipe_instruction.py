from sqlmodel import SQLModel, Field


class RecipeInstructionBase(SQLModel):
    step_number: int
    description: str
    media: str | None = None
    recipe_id: int


class RecipeInstruction(RecipeInstructionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class RecipeInstructionCreate(RecipeInstructionBase):
    pass


class RecipeInstructionRead(RecipeInstructionBase):
    id: int
