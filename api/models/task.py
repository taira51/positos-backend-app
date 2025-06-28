from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.db import Base

#タスクテーブル
class Task(Base):
    __tablename__ = "Task"

    taskId = Column(Integer, primary_key=True)
    taskName = Column(String(50), nullable=False)
    taskStatus = Column(Integer, nullable=False)