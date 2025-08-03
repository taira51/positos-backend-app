from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
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
def get_by_id(db: AsyncSession, project_id: UUID) -> Optional[project_model.Project]:
    return db.query(project_model.Project).filter(project_model.Project.id == project_id).first()

#プロジェクトを全件取得する（TODO 未実装 ⇒ ユーザーIDごとに取得する）
def get_all(db: AsyncSession) -> list[project_model.Project]:
    return db.query(project_model.Project).order_by(project_model.Project.created_at.desc()).all()

#プロジェクトを更新する
def update(db: AsyncSession, project_id, new_name: str) -> Optional[project_model.Project]:
    project = db.query(project_model.Project).filter(project_model.Project.id == project_id).first()
    if project is None:
        return None
    project.name = new_name
    db.commit()
    db.refresh(project)
    return project

#プロジェクトを削除する
def delete(db: AsyncSession, project_id) -> bool:
    project = db.query(project_model.Project).filter(project_model.Project.id == project_id).first()
    if project is None:
        return False
    db.delete(project)
    db.commit()
    return True