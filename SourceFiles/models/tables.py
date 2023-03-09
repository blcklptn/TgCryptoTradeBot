from datetime import datetime
from database.db import Base
from sqlalchemy import Column, String, DateTime, Integer, BigInteger

class Users(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    refferals = Column(Integer, default=0, unique=False)
    refer_id = Column(BigInteger, default=0, unique=False)
    user_id = Column(String, default=None, unique=True)
    username = Column(String, default=None, unique=False)
    balance = Column(BigInteger, default=0, unique=False)
    deals = Column(BigInteger, default=0, unique=False)
    discount = Column(Integer, default=0, unique=False)
    added = Column(DateTime, default=datetime.now())


class Admins(Base):
    __tablename__ = 'Admins'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    user_id = Column(String, default=None, unique=True)
    added = Column(DateTime, default=datetime.now())


class Operators(Base):
    __tablename__ == 'Operators'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    user_id = Column(String, default=None, unique=True)
    added = Column(DateTime, default=datetime.now())