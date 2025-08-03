from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from api.db import get_db
from typing import List

import api.schemas.task as task_schema
import api.cruds.task as task_crud

router = APIRouter(
    prefix="/task",
    tags=["task"]
)

#タスクを全件取得する
@router.get("", response_model=List[task_schema.TaskBase])
async def get_all(db: AsyncSession = Depends(get_db)):
    return await task_crud.get_all(db)

#タスクを作成する
@router.post("", response_model=task_schema.TaskCreateResponse)
async def create(task_body: task_schema.TaskCreate, db: AsyncSession = Depends(get_db)):
    return await task_crud.create(db, task_body)

#タスクを更新する
@router.put("/{task_id}", response_model=task_schema.TaskCreateResponse)
async def update(task_id: int, task_body: task_schema.TaskCreate, db: AsyncSession = Depends(get_db)):
    task = await task_crud.get_by_id(db, task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return await task_crud.update(db, task_body, original=task)

#タスクを削除する
@router.delete("/{task_id}", response_model=None)
async def delete(task_id: int, db: AsyncSession = Depends(get_db)):
    task = await task_crud.get_by_id(db, task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return await task_crud.delete(db, original=task)

#タスクを生成して返却する
@router.post("/generate", response_model=List[task_schema.TaskBase])
async def generateTasks(request: task_schema.PromptRequest):
    return await task_crud.generateTasks(request.prompt)