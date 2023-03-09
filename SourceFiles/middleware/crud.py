from database import db
from models.tables import Users, Admins
from datetime import datetime, timedelta
from core import config
from .error_handler import handle_crud_error

session = db.create_database()

@handle_crud_error
async def add_admin(user_id: str) -> None:
    admin = Admins(user_id=user_id)
    session.add(admin)
    session.commit()

@handle_crud_error
async def add_user(username: str, user_id: str) -> None:
    user = Users(username=username, user_id=user_id)
    session.add(user)
    session.commit()
