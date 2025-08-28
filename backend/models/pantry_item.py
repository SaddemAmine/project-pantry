from datetime import datetime
from sqlmodel import SQLModel, Field


class PantryItemBase(SQLModel):
    expiration_date: datetime | None = None
    quantity: float = 1.0
    unit: str | None = None
    notes: str | None = None
    user_id: int | None = None
    item_id: int | None = None


class PantryItem(PantryItemBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class PantryItemCreate(PantryItemBase):
    pass


class PantryItemRead(PantryItemBase):
    id: int
