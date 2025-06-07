from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from backend.models.item import Item

DATABASE_URL = "postgresql+psycopg2://postgres:@localhost/pantry"

engine = create_engine(DATABASE_URL, echo=True)
session = Session(engine)

session.add(Item(name="Test Item", description="This is a test item."))
