from pydantic import BaseModel

from ..utils.UoM import UoM


class RecipeItem(BaseModel):
    id: int
    quantity: float = 1.0
    unit: UoM | None = None
    notes: str | None = None

    # Relationships
    item_id: int
    recipe_id: int
