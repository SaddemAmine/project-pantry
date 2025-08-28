from datetime import datetime
from sqlmodel import SQLModel, Field


class ItemBase(SQLModel):
    name: str
    description: str | None = None
    image: str | None = None
    time_to_expire: datetime | None = None
    is_generic: bool = False


class Item(ItemBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class ItemCreate(ItemBase):
    pass


class ItemRead(ItemBase):
    id: int
