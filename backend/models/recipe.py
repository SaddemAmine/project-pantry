from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    time_to_cook = Column(Integer, default=0)  # Could be a time delta or timestamp in the future
    image = Column(String, nullable=True)
    servings = Column(Integer, default=1)

    # TODO: Add tags

    # Relationships
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship("User", back_populates="recipes")
    ingredients = relationship("RecipeIngredient", back_populates="recipe")
    instructions = relationship("RecipeInstruction", back_populates="recipe")
