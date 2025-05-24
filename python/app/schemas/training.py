from pydantic import BaseModel, field_validator
from typing import List, Literal

class ExerciseBase(BaseModel):
    name: str
    muscle_group: str
    muscle_size: Literal["large", "small"]
    difficulty: Literal["beginner", "intermediate", "advanced"]
    exercise_type: Literal["compound", "isolation"]

class ExerciseOut(ExerciseBase):
    id: int

    class Config:
        from_attributes = True

class TrainingPlanBase(BaseModel):
    name: str
    split_type: str
    goal: str
    days_per_week: int
    difficulty: str

class TrainingPlanCreate(TrainingPlanBase):
    @field_validator("goal")
    def validate_goal(cls, v):
        allowed = {"Redukcja", "Masa", "Siła"}
        if v.capitalize() not in allowed:
            raise ValueError(f"Nieprawidłowy cel treningowy. Dozwolone: {', '.join(allowed)}")
        return v.capitalize()  

class TrainingPlanOut(TrainingPlanBase):
    id: int
    exercises: List[ExerciseOut] = []
    training_text: str

    class Config:
        from_attributes = True
