from sqlalchemy.orm import Session
from app.models.user import UserInfo

def calculate_bmr(weight: float, height: float, age: int, gender: str) -> float:
    """Obliczanie BMR (Podstawowa Przemiana Materii)"""
    if gender.lower() == "male":
        return (10 * weight) + (6.25 * height) - (5 * age) + 5
    elif gender.lower() == "female":
        return (10 * weight) + (6.25 * height) - (5 * age) - 161
    else:
        return None

def calculate_tdee(bmr: float, activity_level: float) -> float:
    """Obliczanie TDEE na podstawie BMR i współczynnika aktywności"""
    return bmr * activity_level

def calculate_macros(tdee: float, weight: float, goal: str):
    """Obliczanie białka, tłuszczy i węglowodanów dla różnych celów"""
    
    if goal == "cut":
        target_calories = tdee - 500
        protein = round(weight * 2.2, 2)
        fats = round(weight * 0.8, 2)
    elif goal == "bulk": 
        target_calories = tdee + 500
        protein = round(weight * 2.5, 2)
        fats = round(weight * 1.2, 2)
    else: 
        target_calories = tdee
        protein = round(weight * 1.8, 2) 
        fats = round(weight * 1.0, 2) 

    remaining_calories = target_calories - (protein * 4 + fats * 9)
    carbs = round(remaining_calories / 4, 2)  

    return {
        "calories": round(target_calories, 2),
        "protein": protein,
        "fats": fats,
        "carbs": carbs
    }

def get_caloric_needs(db: Session, user_id: int, activity_level: float):
    """Obliczanie kalorii i makroskładników dla użytkownika"""
    user_info = db.query(UserInfo).filter(UserInfo.user_id == user_id).first()
    if not user_info or not user_info.weight or not user_info.height or not user_info.age or not user_info.gender:
        return None  

    bmr = calculate_bmr(user_info.weight, user_info.height, user_info.age, user_info.gender)
    if not bmr:
        return None  

    tdee = calculate_tdee(bmr, activity_level)

    return {
        "macros": {
            "cut": calculate_macros(tdee, user_info.weight, "cut"),
            "maintenance": calculate_macros(tdee, user_info.weight, "maintenance"),
            "bulk": calculate_macros(tdee, user_info.weight, "bulk")
        }
    }
