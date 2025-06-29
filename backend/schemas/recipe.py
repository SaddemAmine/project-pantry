from pydantic import BaseModel


class Recipe(BaseModel):
    id: int
    name: str
    description: str | None = None
    time_to_cook: int = 0           # Would it be interesting for this to be a time delta / timestamp?
    instructions: str               # How to model the relationship with instructions ?
    servings: int = 1
    image: str | None = None
    tags: list[int] | None = None

    # Relationships
    user_id: int | None = None
