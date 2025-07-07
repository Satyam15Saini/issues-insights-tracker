from pydantic import BaseModel

class IssueBase(BaseModel):
    title: str
    description: str
    severity: str

class IssueCreate(IssueBase):
    pass

class Issue(IssueBase):
    id: int
    status: str

    class Config:
        orm_mode = True
