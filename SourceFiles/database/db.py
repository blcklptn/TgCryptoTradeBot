from core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL to our database container
SQLALCHEMY_DATABASE_URL = f'postgresql://test:test@localhost:5432/testbase'  # noqa: E501, WPS326, WPS221

# sqlalchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def create_database():
    '''
    Creates tables in our database and returns local session.
    '''
    Base.metadata.create_all(bind=engine)
    return SessionLocal()