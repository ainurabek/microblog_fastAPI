from core.db import Base
from sqlalchemy import Column, INTEGER, String, TEXT, DateTime, Boolean

class User(Base):
    __tablename__ = 'user'

    id = Column(INTEGER, unique=True, primary_key=True, index=True)
    username = Column(String, unique=True,)
    email = Column(String, unique=True, )
    password = Column(String)
    created_at = Column(DateTime)
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)

