from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result
from typing import Optional, Tuple
from uuid import UUID, uuid4

import api.models.project as project_model
import api.schemas.project as project_schema

#プロジェクトを作成する
async def create(db: AsyncSession, create: project_schema.ProjectCreate) -> project_model.Project:
    project = project_model.Project(**create.dict())
    project.projectId = uuid4()
    db.add(project)
    await db.commit()
    await db.refresh(project)
    return project

#プロジェクトを1件取得する
async def get_by_id(db: AsyncSession, project_id: UUID) -> Optional[project_model.Project]:
    result: Result = await db.execute(
        select(project_model.Project).filter(project_model.Project.projectId == str(project_id))
    )
    project: Optional[Tuple[project_model.Project]] = result.first()
    return project[0] if project is not None else None  # 要素が一つであってもtupleで返却されるので１つ目の要素を取り出す

#プロジェクトを全件取得する（TODO 未実装 ⇒ ユーザーIDごとに取得する）
async def get_all(db: AsyncSession) -> list[project_model.Project]:
    result: Result = await db.execute(
        select(project_model.Project).order_by(project_model.Project.created_at.desc())
    )
    return result.scalars().all()

#プロジェクトを更新する
async def update(db: AsyncSession, project_id: UUID, new_name: str) -> Optional[project_model.Project]:
    result: Result = await db.execute(
        select(project_model.Project).filter(project_model.Project.projectId == project_id)
    )
    project: Optional[project_model.Project] = result.scalar_one_or_none()
    if project is None:
        return None
    project.name = new_name
    await db.commit()
    await db.refresh(project)
    return project

#プロジェクトを削除する
async def delete(db: AsyncSession, project_id: UUID) -> bool:
    result: Result = await db.execute(
        select(project_model.Project).filter(project_model.Project.projectId == project_id)
    )
    project: Optional[project_model.Project] = result.scalar_one_or_none()
    if project is None:
        return False
    await db.delete(project)
    await db.commit()
    return True