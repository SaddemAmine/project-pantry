from datetime import datetime
from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
    description: str | None = None
    image: str | None = None
    time_to_expire: datetime | None = None
    is_generic: bool = False
