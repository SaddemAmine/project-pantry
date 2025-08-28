from sqlmodel import SQLModel, Field


class UserBase(SQLModel):
    username: str
    email: str | None = None


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: int
