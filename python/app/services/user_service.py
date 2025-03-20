from sqlalchemy.orm import Session
from app.models.user import User, UserInfo
from app.schemas.user import UserCreate, UserInfoCreate

def create_user_info(db: Session, user_id: int, info_data: UserInfoCreate):
    """Dodanie informacji o użytkowniku"""
    user_info = UserInfo(user_id=user_id, **info_data.dict())
    db.add(user_info)
    db.commit()
    db.refresh(user_info)
    return user_info

def get_user_info(db: Session, user_id: int):
    """Pobranie informacji o użytkowniku"""
    return db.query(UserInfo).filter(UserInfo.user_id == user_id).first()

def update_user_info(db: Session, user_id: int, info_data: UserInfoCreate):
    """Aktualizacja informacji o użytkowniku"""
    user_info = db.query(UserInfo).filter(UserInfo.user_id == user_id).first()
    if not user_info:
        return None  

    for key, value in info_data.dict(exclude_unset=True).items():
        setattr(user_info, key, value)  

    db.commit()
    db.refresh(user_info)
    return user_info

def delete_user_info(db: Session, user_id: int):
    """Usunięcie informacji o użytkowniku"""
    user_info = db.query(UserInfo).filter(UserInfo.user_id == user_id).first()
    if not user_info:
        return None 

    db.delete(user_info)
    db.commit()
    return True