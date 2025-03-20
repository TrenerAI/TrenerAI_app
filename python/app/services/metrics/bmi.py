from sqlalchemy.orm import Session
from app.models.user import UserInfo

def calculate_bmi(db: Session, user_id: int):
    """Obliczanie BMI dla użytkownika"""
    user_info = db.query(UserInfo).filter(UserInfo.user_id == user_id).first()
    
    if not user_info:
        return None  
    if not user_info.weight or not user_info.height:
        return None  

    height_in_meters = user_info.height / 100
    bmi = user_info.weight / (height_in_meters ** 2)

    bmi_category = interpret_bmi(bmi)

    return {
        "bmi": round(bmi, 2),
        "category": bmi_category
    }

def interpret_bmi(bmi: float):
    """Klasyfikacja BMI według WHO"""
    if bmi < 18.5:
        return "Niedowaga"
    elif 18.5 <= bmi < 24.9:
        return "Prawidłowa waga"
    elif 25 <= bmi < 29.9:
        return "Nadwaga"
    else:
        return "Otyłość"
