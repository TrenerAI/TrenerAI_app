from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.metrics.bmi import calculate_bmi
from app.services.metrics.tdee import get_caloric_needs
from app.services.metrics.rpe import calculate_rpe

router = APIRouter()

@router.get("/{user_id}/bmi")
def get_user_bmi(user_id: int, db: Session = Depends(get_db)):
    bmi_data = calculate_bmi(db, user_id)
    if not bmi_data:
        raise HTTPException(status_code=404, detail="Brak danych do obliczenia BMI")
    return bmi_data

@router.get("/{user_id}/calories")
def get_user_caloric_needs(user_id: int, activity_level: float, db: Session = Depends(get_db)):
    caloric_data = get_caloric_needs(db, user_id, activity_level)
    if not caloric_data:
        raise HTTPException(status_code=404, detail="Brak danych do obliczenia kalorii")
    return caloric_data

@router.get("/rpe")
def get_rpe(rir: int):
    """
    Oblicza RPE (Rate of Perceived Exertion) na podstawie RIR (Reps in Reserve).
    
    - **RIR 0** → RPE 10 (maksymalny wysiłek)
    - **RIR 2** → RPE 8
    - **RIR 4** → RPE 6
    """
    if rir < 0:
        raise HTTPException(status_code=400, detail="RIR nie może być ujemny!")
    
    rpe = calculate_rpe(rir)
    return {"RIR": rir, "RPE": rpe}