from sqlalchemy import Column, Integer, String, Enum, JSON, Text
from app.core.database import Base
from enum import Enum as PyEnum

class MuscleSize(PyEnum):
    LARGE = "large"
    SMALL = "small"

class MovementType(PyEnum):
    PUSH = "Push"
    PULL = "Pull"
    ISOLATION = "Isolation"

class DifficultyLevel(PyEnum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"

class ExerciseType(PyEnum):
    COMPOUND = "compound"
    ISOLATION = "isolation"

class Exercise(Base):
    """Tabela ćwiczeń"""
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    muscle_group = Column(String, nullable=False)
    muscle_size = Column(Enum(MuscleSize), nullable=False)
    movement_type = Column(Enum(MovementType), nullable=False)
    difficulty = Column(Enum(DifficultyLevel), nullable=False)
    exercise_type = Column(Enum(ExerciseType), nullable=False)
    recommended_reps = Column(JSON, nullable=False)  # { "masa": "6-12", "siła": "3-6", "redukcja": "12-15" }
    recommended_sets = Column(JSON, nullable=False)  # { "beginner": "3", "intermediate": "4", "advanced": "5" }
    rest_time = Column(Integer, nullable=False)  # Czas przerwy w sekundach
    description = Column(Text, nullable=True)
