from typing import Optional
from pydantic import BaseModel
from datetime import datetime

#BaseModel（共通項目
class ProjectBase(BaseModel):
    projectId: Optional[str] = None
    projectName: Optional[str] = None
    projectOrder: Optional[int] = None
    createUserId: Optional[str] = None
    createDateTime: Optional[datetime] = None
    updateUserId: Optional[str] = None
    updateDateTime: Optional[datetime] = None

#プロジェクト（POSTリクエスト）
class ProjectCreate(ProjectBase):
    projectName: str

#プロジェクト（POSTレスポンス）
class ProjectCreateResponse(ProjectBase):
    class Config:
        orm_mode = True
