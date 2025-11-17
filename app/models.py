from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base

class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    short = Column(String, unique=True, index=True)
    long = Column(String)
    clicks = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_accessed = Column(DateTime, default=datetime.utcnow)
