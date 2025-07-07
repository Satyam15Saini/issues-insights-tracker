from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app import database, models, auth

router = APIRouter()

@router.post("/register")
def register(email: str, password: str, db: Session = Depends(database.SessionLocal)):
    hashed_pw = auth.get_password_hash(password)
    user = models.User(email=email, hashed_password=hashed_pw)
    db.add(user)
    db.commit()
    return {"msg": "User created"}

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.SessionLocal)):
    user = db.query(models.User).filter(models.User.email == form_data.username).first()
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = auth.create_access_token({"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
