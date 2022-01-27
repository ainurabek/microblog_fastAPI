from sqlalchemy.orm import relationship

from core.db import Base
from sqlalchemy import Column, Integer, String, TEXT, DateTime, ForeignKey

class Post(Base):
    __tablename__ = 'microblog_posts'
    id = Column(Integer, unique=True, primary_key=True, index=True)
    title = Column(String)
    text = Column(String(350))
    date = Column(DateTime)
    user = Column(Integer, ForeignKey("user.id"))
    user_id = relationship("user")
