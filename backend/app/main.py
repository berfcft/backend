from fastapi import FastAPI
from app.routes.users import router as user_router
from app.database import Base, engine  
from app import models

models.Base.metadata.create_all(bind=engine)

# Uygulama nesnesi
app = FastAPI()

# Kullanıcı router'ını ekle
app.include_router(user_router, prefix="/auth", tags=["Auth"])
