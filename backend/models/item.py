from sqlalchemy import Column, Integer, String, Boolean, DateTime
from ..database import Base

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String, nullable=True)
    image = Column(String, nullable=True)
    time_to_expire = Column(DateTime, nullable=True)
    is_generic = Column(Boolean, default=False)
