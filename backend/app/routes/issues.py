from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from deps import get_db, require_role
from auth import get_current_user

router = APIRouter()

@router.post("/issues/", dependencies=[Depends(require_role("REPORTER"))])
def create_issue(issue: schemas.IssueCreate, db: Session = Depends(get_db)):
    db_issue = models.Issue(**issue.dict())
    db.add(db_issue)
    db.commit()
    return db_issue

@router.get("/issues/")
def list_issues(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(models.Issue).all()
