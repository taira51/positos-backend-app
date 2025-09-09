from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from api.db import get_db

import api.schemas.project as project_schema
import api.cruds.project as project_crud

router = APIRouter(
    prefix="/project",
    tags=["project"]
)

#プロジェクトを作成する
@router.post("", response_model=project_schema.ProjectCreateResponse)
async def create(
    project_create: project_schema.ProjectCreate,
    db: AsyncSession = Depends(get_db)
):
    return await project_crud.create(db, project_create)

#プロジェクトを1件取得する
@router.get("/{projectId}", response_model=project_schema.ProjectBase)
async def get(
    projectId: UUID,
    db: AsyncSession = Depends(get_db)
):
    project = await project_crud.get_by_id(db, projectId)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

# #プロジェクトを全件取得する（TODO 未実装 ⇒ ユーザーIDごとに取得する）
# @router.get("/", response_model=list[project_schema.ProjectResponse])
# async def list_projects(db: AsyncSession = Depends(get_db)):
#     return project_crud.get_all_projects(db)

# # プロジェクトを更新する
# @router.put("/{projectId}", response_model=project_schema.ProjectResponse)
# async def update_project(
#     projectId: UUID,
#     project_update: project_schema.ProjectCreate,
#     db: AsyncSession = Depends(get_db)
# ):
#     updated = project_crud.update(db, projectId, project_update.name)
#     if updated is None:
#         raise HTTPException(status_code=404, detail="Project not found")
#     return updated

# # プロジェクトを削除する
# @router.delete("/{projectId}", status_code=204)
# def delete_project(
#     projectId: UUID,
#     db: AsyncSession = Depends(get_db)
# ):
#     success = project_crud.delete(db, projectId)
#     if not success:
#         raise HTTPException(status_code=404, detail="Project not found")