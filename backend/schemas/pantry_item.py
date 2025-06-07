from datetime import datetime
from pydantic import BaseModel

from ..utils.UoM import UoM


class PantryItem(BaseModel):
    id: int
    expiration_date: datetime | None = None
    quantity: float = 1.0
    unit: UoM | None = None
    notes: dict[str, str] | None = None

    # Relationships
    user_id: int | None = None
    item_id: int | None = None
