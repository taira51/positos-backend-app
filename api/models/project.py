from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.dialects.mysql import CHAR
from datetime import datetime
from zoneinfo import ZoneInfo
import uuid

from api.db import Base

#プロジェクトテーブル
class Project(Base):
    __tablename__ = "Project"

    # 主キー（UUID）
    projectId = Column(CHAR(36), primary_key=True, default=uuid.uuid4)

    # プロジェクト名（必須）
    projectName = Column(String(255), nullable=False)

    # プロジェクト順番
    projectOrder = Column(Integer, nullable=True)

    # 作成者ユーザーID（Firebase UID、任意）
    createUserId = Column(String(128), nullable=True)

    # 作成日時（必須）
    createDateTime = Column(DateTime, nullable=False, default=lambda: datetime.now(ZoneInfo("Asia/Tokyo")))

    # 更新ユーザーID（Firebase UID、任意）
    updateUserId = Column(String(128), nullable=True)

    # 更新日時（必須）
    updateDateTime = Column(DateTime, nullable=False, default=lambda: datetime.now(ZoneInfo("Asia/Tokyo")), onupdate=lambda: datetime.now(ZoneInfo("Asia/Tokyo")))
