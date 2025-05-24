from sqlalchemy import Column, Integer, String, Enum
from app.core.database import Base
from enum import Enum as PyEnum

class MuscleSize(PyEnum):
    LARGE = "large"
    SMALL = "small"

class DifficultyLevel(PyEnum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"

class ExerciseType(PyEnum):
    COMPOUND = "compound"
    ISOLATION = "isolation"

class Exercise(Base):
    """Uproszczona tabela ćwiczeń (demo FBW)"""
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    muscle_group = Column(String, nullable=False)
    muscle_size = Column(Enum(MuscleSize), nullable=False)
    difficulty = Column(Enum(DifficultyLevel), nullable=False)
    exercise_type = Column(Enum(ExerciseType), nullable=False)
