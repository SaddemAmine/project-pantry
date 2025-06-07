from sqlalchemy import Column, Float, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base


class RecipeItem(Base):
    __tablename__ = 'recipe_items'

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Float, nullable=False, default=1)
    unit = Column(String, nullable=True)  # Assuming UoM is stored as a string
    notes = Column(String, nullable=True)

    # Relationships
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    recipe_id = Column(Integer, ForeignKey('recipes.id'), nullable=False)

    item = relationship("Item", back_populates="recipe_items")
    recipe = relationship("Recipe", back_populates="items")
