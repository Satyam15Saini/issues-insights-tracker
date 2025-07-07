from sqlalchemy.orm import Session
from app import models, schemas

def create_issue(db: Session, issue: schemas.IssueCreate):
    db_issue = models.Issue(**issue.dict())
    db.add(db_issue)
    db.commit()
    db.refresh(db_issue)
    return db_issue

def get_issues(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Issue).offset(skip).limit(limit).all()
