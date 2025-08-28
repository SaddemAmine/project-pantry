from sqlmodel import SQLModel, Field


class RecipeBase(SQLModel):
    name: str
    description: str | None = None
    time_to_cook: int = 0
    image: str | None = None
    servings: int = 1
    user_id: int | None = None


class Recipe(RecipeBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class RecipeCreate(RecipeBase):
    pass


class RecipeRead(RecipeBase):
    id: int
