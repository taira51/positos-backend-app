from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey

# BaseModel（共通項目）
class TaskBase(BaseModel):
    taskId: Optional[int] = None
    taskName: Optional[str] = None
    taskStatus: Optional[int] = None
    taskOrder: Optional[int] = None
    taskMemo: Optional[str] = None
    taskDeadline: Optional[datetime] = None
    taskCompletedUserId: Optional[str] = None
    createUserId: Optional[str] = None
    createDateTime: Optional[datetime] = None
    updateUserId: Optional[str] = None
    updateDateTime: Optional[datetime] = None

# タスク（POSTリクエスト）
class TaskCreate(TaskBase):
    pass

# タスク（POSTレスポンス）
class TaskCreateResponse(TaskCreate):
    taskId: int
    createDateTime: datetime

    class Config:
        orm_mode = True

# タスク（PUTリクエスト）
class TaskUpdate(BaseModel):
    taskId: int
    updateUserId: str

# タスク（PUTレスポンス）
class TaskUpdate(BaseModel):
    taskId: int

    class Config:
        orm_mode = True

# タスク生成プロンプト
class PromptRequest(BaseModel):
    prompt: str