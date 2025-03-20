from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.user import UserInfoCreate, UserInfoOut, UserOut, UserUpdate
from app.services.user_service import create_user_info, delete_user_info, get_user_info, update_user, update_user_info

router = APIRouter()

@router.post("/{user_id}/info", response_model=UserInfoOut)
def add_user_info(user_id: int, info_data: UserInfoCreate, db: Session = Depends(get_db)):
    """Dodanie informacji o użytkowniku"""
    return create_user_info(db, user_id, info_data)

@router.get("/{user_id}/info", response_model=UserInfoOut)
def read_user_info(user_id: int, db: Session = Depends(get_db)):
    """Pobranie informacji o użytkowniku"""
    info = get_user_info(db, user_id)
    if not info:
        raise HTTPException(status_code=404, detail="User info not found")
    return info

@router.put("/{user_id}", response_model=UserOut)
def update_user_endpoint(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db)):
    """Aktualizacja użytkownika (full_name)"""
    updated_user = update_user(db, user_id, user_data)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.put("/{user_id}/info", response_model=UserInfoOut)
def update_user_info_endpoint(user_id: int, info_data: UserInfoCreate, db: Session = Depends(get_db)):
    """Aktualizacja informacji o użytkowniku"""
    updated_info = update_user_info(db, user_id, info_data)
    if not updated_info:
        raise HTTPException(status_code=404, detail="User info not found")
    return updated_info

@router.delete("/{user_id}/info")
def delete_user_info_endpoint(user_id: int, db: Session = Depends(get_db)):
    """Usunięcie informacji o użytkowniku"""
    success = delete_user_info(db, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User info not found")
    return {"message": "User info deleted successfully"}