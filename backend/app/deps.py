from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
import database, models
from auth import get_current_user

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def require_role(required_role: str):
    def role_dependency(current_user: models.User = Depends(get_current_user)):
        if current_user.role != required_role and current_user.role != "ADMIN":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Not enough permissions. Requires {required_role}",
            )
        return current_user
    return role_dependency
