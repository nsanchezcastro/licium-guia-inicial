from app.core.base import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID 
from app.core.registry import register_model
import datetime

class Checklist(Base):
    __tablename__ = "practice_checklist" 
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String) 
    status = Column(String(50), default="open")
    is_public = Column(Boolean, default=False)
    closed_at = Column(DateTime(timezone=True))
    owner_id = Column(UUID(as_uuid=True), ForeignKey("core_user.id"))

   
    items = relationship("ChecklistItem", back_populates="checklist", cascade="all, delete-orphan")

class ChecklistItem(Base):
    __tablename__ = "practice_checklist_item"
    
    id = Column(Integer, primary_key=True)
    checklist_id = Column(Integer, ForeignKey("practice_checklist.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(255), nullable=False)
    is_done = Column(Boolean, default=False)
    done_at = Column(DateTime(timezone=True))
    assigned_user_id = Column(UUID(as_uuid=True), ForeignKey("core_user.id"))
    priority = Column(String(20), default="medium")

    
    checklist = relationship("Checklist", back_populates="items")


register_model(Checklist)
register_model(ChecklistItem)