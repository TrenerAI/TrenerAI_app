from fastapi import APIRouter, Depends, HTTPException, Path, Request, Response
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse
from authlib.integrations.starlette_client import OAuth
from app.schemas.user import UserCreate, UserOut
from app.services.auth_service import create_user, authenticate_user
from app.core.database import get_db
from app.models.user import User
from app.config.settings import settings
import logging

router = APIRouter()

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

@router.post("/register", response_model=UserOut)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    """Rejestracja użytkownika za pomocą e-maila i hasła"""
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db, user_data)

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """Logowanie użytkownika za pomocą e-maila i hasła"""
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return {"message": "Login successful", "user_id": user.id, "email": user.email}

@router.delete("/users/{user_id}", status_code=204)
def delete_user_by_id(
    user_id: int = Path(..., gt=0),
    db: Session = Depends(get_db)
):
    """Usuwa użytkownika i jego powiązane dane (UserInfo, TrainingPlan)"""
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="Użytkownik nie został znaleziony")

    try:
        for plan in user.training_plans:
            db.delete(plan)
        if user.user_info:
            db.delete(user.user_info)
        db.delete(user)
        db.commit()

        return Response(status_code=204)

    except Exception as e:
        logger.error(f"Błąd podczas usuwania użytkownika ID {user_id}: {e}")
        raise HTTPException(status_code=500, detail="Wystąpił błąd podczas usuwania użytkownika")

oauth = OAuth()
oauth.register(
     name="google",
    client_id=settings.GOOGLE_CLIENT_ID,
    client_secret=settings.GOOGLE_CLIENT_SECRET,
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)

@router.get("/login/google")
async def login_google(request: Request):
    """Przekierowanie użytkownika do logowania przez Google"""
    try:
        return await oauth.google.authorize_redirect(request, "http://127.0.0.1:8088/auth/google/callback")
    except Exception as e:
        logger.error(f"Błąd podczas przekierowania do Google OAuth: {e}")
        raise HTTPException(status_code=500, detail="Błąd podczas logowania przez Google")

@router.get("/google/callback")
async def google_callback(request: Request, db: Session = Depends(get_db)):
    """Obsługa logowania przez Google po przekierowaniu"""
    try:
        token = await oauth.google.authorize_access_token(request)
        user_info = token.get("userinfo")

        if not user_info:
            raise HTTPException(status_code=400, detail="Google authentication failed")

        user = db.query(User).filter(User.email == user_info["email"]).first()
        if not user:
            user = User(
                email=user_info["email"],
                full_name=user_info["name"],
                google_id=user_info["sub"]
            )
            db.add(user)
            db.commit()
            db.refresh(user)

        return {"message": "Google login successful", "user": {"email": user.email, "name": user.full_name}}
    
    except Exception as e:
        logger.error(f"Błąd podczas logowania przez Google: {e}")
        raise HTTPException(status_code=500, detail="Błąd podczas autoryzacji Google")