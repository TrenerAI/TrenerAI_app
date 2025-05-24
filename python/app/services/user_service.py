from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.user import User, UserInfo
from app.schemas.user import UserInfoCreate, UserUpdate


def create_user_info(db: Session, user_id: int, info_data: UserInfoCreate):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    existing_info = db.query(UserInfo).filter(UserInfo.user_id == user_id).first()
    if existing_info:
        raise HTTPException(status_code=400, detail="User info already exists")

    user_info = UserInfo(user_id=user_id, **info_data.model_dump())
    db.add(user_info)
    db.commit()
    db.refresh(user_info)
    return user_info


def get_user_info(db: Session, user_id: int):
    info = db.query(UserInfo).filter(UserInfo.user_id == user_id).first()
    if not info:
        raise HTTPException(status_code=404, detail="User info not found")
    return info


def update_user(db: Session, user_id: int, user_data: UserUpdate):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    for key, value in user_data.model_dump(exclude_unset=True).items():
        if hasattr(user, key):
            setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user


def update_user_info(db: Session, user_id: int, info_data: UserInfoCreate):
    user_info = db.query(UserInfo).filter(UserInfo.user_id == user_id).first()
    if not user_info:
        raise HTTPException(status_code=404, detail="User info not found")

    for key, value in info_data.model_dump(exclude_unset=True).items():
        if hasattr(user_info, key):
            setattr(user_info, key, value)

    db.commit()
    db.refresh(user_info)
    return user_info


def delete_user_info(db: Session, user_id: int):
    user_info = db.query(UserInfo).filter(UserInfo.user_id == user_id).first()
    if not user_info:
        raise HTTPException(status_code=404, detail="User info not found")

    db.delete(user_info)
    db.commit()
    return True
