from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Tuple, Optional

from sqlalchemy import select
from sqlalchemy.engine import Result

from datetime import datetime

import api.models.task as task_model
import api.schemas.task as task_schema

#タスクを作成する
async def create(
    db: AsyncSession, create: task_schema.TaskCreate
) -> task_model.Task:
    task = task_model.Task(**create.dict())
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task

#タスクを全件取得する
async def get_all(db: AsyncSession) -> List[Tuple[int, str, int]]:
    result: Result = await (
        db.execute(
            select(
                task_model.Task.taskId,
                task_model.Task.taskName,
                task_model.Task.taskStatus,
                task_model.Task.taskOrder,
                task_model.Task.createUserId,
                task_model.Task.createDateTime,
            )
        )
    )
    return result.all()

#タスクを1件取得する
async def get_by_id(db: AsyncSession, task_id: int) -> Optional[task_model.Task]:
    result: Result = await db.execute(
        select(task_model.Task).filter(task_model.Task.taskId == task_id)
    )
    task: Optional[Tuple[task_model.Task]] = result.first()
    return task[0] if task is not None else None  # 要素が一つであってもtupleで返却されるので１つ目の要素を取り出す

#タスクを1件更新する
async def update(db: AsyncSession, task_create: task_schema.TaskCreate, original: task_model.Task) -> task_model.Task:
    original.taskName = task_create.taskName
    original.taskStatus = task_create.taskStatus
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original

#タスクを1件更新する
async def delete(db: AsyncSession, original: task_model.Task) -> None:
    await db.delete(original)
    await db.commit()

#タスクをChatGPT APIで生成する
async def generateTasks(prompt: str) -> List[task_schema.TaskBase]:
    #TODO ChatGPT連携（モックとして仮のタスクを生成して返却する）
    generated = [
        {"taskId": 1, "taskName": "生成されたタスク３", "taskStatus": 1, "taskOrder": 0, "taskMemo": "生成されたタスクメモ３", "taskDeadline": None, "taskCompletedUserId": None, "createUserId": "Aさん", "createDateTime": datetime(2025, 7, 13, 19, 51, 8)},
        {"taskId": 2, "taskName": "生成されたタスク４", "taskStatus": 1, "taskOrder": 0, "taskMemo": "生成されたタスクメモ４", "taskDeadline": None, "taskCompletedUserId": None, "createUserId": "Aさん", "createDateTime": datetime(2025, 7, 13, 19, 51, 8)},
        {"taskId": 3, "taskName": "生成されたタスク５", "taskStatus": 1, "taskOrder": 0, "taskMemo": "生成されたタスクメモ５", "taskDeadline": None, "taskCompletedUserId": None, "createUserId": "Aさん", "createDateTime": datetime(2025, 7, 13, 19, 51, 8)},
    ]
    return [task_schema.TaskBase(**t) for t in generated]
