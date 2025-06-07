from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base


class RecipeInstruction(Base):
    __tablename__ = 'recipe_instructions'

    id = Column(Integer, primary_key=True, index=True)
    step_number = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    media = Column(String, nullable=True)  # URL or path to media file

    # Relationships
    recipe_id = Column(Integer, ForeignKey('recipes.id'), nullable=False)

    recipe = relationship("Recipe", back_populates="instructions")
