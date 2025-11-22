from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime
from database import Base

class Tasks(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    task = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    status = Column(Boolean, nullable=False)
    created_at = Column(DateTime, nullable=False)