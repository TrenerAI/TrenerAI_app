from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=64, description="Hasło musi mieć min. 8 znaków")


class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: Optional[str] = None

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    full_name: Optional[str] = Field(None, min_length=2, max_length=100)

    @field_validator("full_name")
    @classmethod
    def name_must_not_be_blank(cls, v):
        if v is not None and not v.strip():
            raise ValueError("Imię i nazwisko nie mogą być puste")
        return v

class UserInfoBase(BaseModel):
    age: Optional[int] = Field(None, ge=0, le=120)
    weight: Optional[float] = Field(None, gt=0, le=300)
    height: Optional[float] = Field(None, gt=0, le=250)
    gender: Optional[str] = Field(None, pattern="^(male|female|other)$")

    @field_validator("gender")
    @classmethod
    def gender_lowercase(cls, v):
        if v:
            return v.lower()
        return v

class UserInfoCreate(UserInfoBase):
    pass

class UserInfoOut(UserInfoBase):
    id: int

    class Config:
        from_attributes = True
