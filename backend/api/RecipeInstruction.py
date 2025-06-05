from pydantic import BaseModel


class RecipeInstruction(BaseModel):
    id: int
    step_number: int
    description: str
    media: str | None = None

    # Relationships
    recipe_id: int
