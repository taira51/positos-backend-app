from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

from api.db import Base

#タスクテーブル
class Task(Base):
    __tablename__ = "Task"

    #タスクID（自動採番される通番）
    taskId = Column(Integer, primary_key=True)

    #タスク名
    taskName = Column(String(50), nullable=False)

    #タスクステータス（１：未着手、２：作業中、３：完了）
    taskStatus = Column(Integer, nullable=False)

    # タスク順番
    taskOrder = Column(Integer, nullable=False)

    # タスクメモ
    taskMemo = Column(String(255), nullable=True)

    # タスク期限日時
    taskDeadline = Column(DateTime, nullable=True)

    # タスク完了者ID（Firebase UID）
    taskCompletedUserId = Column(String(128), nullable=True)

    # 作成者ユーザーID（Firebase UID）
    createUserId = Column(String(128), nullable=False)

    # 作成日時
    createDateTime = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))

    # 更新ユーザーID（Firebase UID）
    updateUserId = Column(String(128), nullable=True)

    # 更新日時
    updateDateTime = Column(DateTime, nullable=True, onupdate=lambda: datetime.now(timezone.utc))