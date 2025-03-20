from pydantic import BaseModel
from typing import List, Dict

class ExerciseBase(BaseModel):
    name: str
    muscle_group: str
    muscle_size: str
    movement_type: str
    difficulty: str
    exercise_type: str
    recommended_reps: Dict[str, str]
    recommended_sets: Dict[str, str]
    rest_time: int

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
    pass

class TrainingPlanOut(TrainingPlanBase):
    id: int
    exercises: List[ExerciseOut] = []
    training_text: str

    class Config:
        from_attributes = True
