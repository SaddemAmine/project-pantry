from sqlmodel import SQLModel, Field


class RecipeItemBase(SQLModel):
    quantity: float = 1.0
    unit: str | None = None
    notes: str | None = None
    item_id: int
    recipe_id: int


class RecipeItem(RecipeItemBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class RecipeItemCreate(RecipeItemBase):
    pass


class RecipeItemRead(RecipeItemBase):
    id: int
