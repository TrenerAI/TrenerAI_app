from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.core.database import Base

class TrainingPlan(Base):
    """Tabela planów treningowych"""
    __tablename__ = "training_plans"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String, nullable=False)
    split_type = Column(String, nullable=False)
    goal = Column(String, nullable=False)
    days_per_week = Column(Integer, nullable=False)
    difficulty = Column(String, nullable=False)
    text_description = Column(Text, nullable=False)

    user = relationship("User", back_populates="training_plans")
    exercises = relationship("TrainingPlanExercise", back_populates="training_plan")

class TrainingPlanExercise(Base):
    """Tabela łącząca plany treningowe z ćwiczeniami"""
    __tablename__ = "training_plan_exercises"

    id = Column(Integer, primary_key=True, index=True)
    training_plan_id = Column(Integer, ForeignKey("training_plans.id"), nullable=False)
    exercise_id = Column(Integer, ForeignKey("exercises.id"), nullable=False)

    training_plan = relationship("TrainingPlan", back_populates="exercises")
    exercise = relationship("Exercise")
