from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class PantryItem(Base):
    __tablename__ = 'pantry_items'

    id = Column(Integer, primary_key=True, index=True)
    expiration_date = Column(String, nullable=True)  # Switch to a delta ?
    quantity = Column(Integer, default=1)
    unit = Column(String, nullable=True)  # Enum in db ?
    notes = Column(String, nullable=True)

    # Relationships
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=True)

    user = relationship("User", back_populates="pantry_items")
    item = relationship("Item", back_populates="pantry_items")
