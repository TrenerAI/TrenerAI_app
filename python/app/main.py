from fastapi import FastAPI
from app.routes import auth, user
from starlette.middleware.sessions import SessionMiddleware
from app.core.database import Base, engine
from app.config.settings import settings
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import sys

app = FastAPI(
    title="TrenerAI",
    description="API for TrenerAI",
    version="1.0.0",
)

app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(user.router, prefix="/api", tags=["UserInfo"])

if __name__ == "__main__" or getattr(sys, "frozen", False):
    uvicorn.run(app, host="127.0.0.1", port=8000)