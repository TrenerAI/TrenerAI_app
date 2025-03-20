from fastapi import APIRouter, Depends
from fastapi.responses import PlainTextResponse
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.training_service import generate_training_plan
from app.schemas.training import TrainingPlanCreate

router = APIRouter()

@router.post("/create", response_class=PlainTextResponse)
def create_training_plan(user_id: int, plan_data: TrainingPlanCreate, db: Session = Depends(get_db)):
    return generate_training_plan(db, user_id, plan_data)
