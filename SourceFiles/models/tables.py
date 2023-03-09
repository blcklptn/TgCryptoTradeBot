from datetime import datetime
from database.db import Base
from sqlalchemy import Column, String, DateTime, Integer, BigInteger

class Users(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    user_id = Column(String, default = None, unique=True)
    username = Column(String, default = None)
    role = Column(String, default='user')
    added = Column(DateTime, default=datetime.now())

