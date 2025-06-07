import os
from fastapi import APIRouter, BackgroundTasks, Depends
from fastapi.responses import FileResponse, JSONResponse, StreamingResponse
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.training_service import generate_training_plan_demo_fbw
from app.schemas.training import TrainingPlanCreate

router = APIRouter()

@router.post("/create", response_class=JSONResponse)
def create_training_plan(user_id: int, plan_data: TrainingPlanCreate, db: Session = Depends(get_db)):
    return generate_training_plan_demo_fbw(db, user_id, plan_data)

@router.post("/create-fbw-pdf")
def create_training_plan_with_pdf(
    user_id: int,
    plan_data: TrainingPlanCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    result = generate_training_plan_demo_fbw(db, user_id, plan_data)
    if isinstance(result, JSONResponse):
        return result

    pdf_path = result["pdf_path"]
    background_tasks.add_task(os.remove, pdf_path)

    file_like = open(pdf_path, mode="rb")
    return StreamingResponse(
        file_like,
        media_type="application/pdf",
        headers={"Content-Disposition": f'attachment; filename="{plan_data.name}_plan.pdf"'},
        background=background_tasks
    )