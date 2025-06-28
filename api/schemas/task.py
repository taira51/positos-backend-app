from typing import Optional
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, ForeignKey

#BaseModel
class TaskBase(BaseModel):
    taskName: str
    taskStatus: int

#タスク（POSTリクエスト）
class TaskCreate(TaskBase):
    pass

#タスク（POSTレスポンス）
class TaskCreateResponse(TaskCreate):
    taskId: int

    class Config:
        orm_mode = True

#タスク（GETレスポンス）
class TaskGet(TaskBase):
    taskId: int
