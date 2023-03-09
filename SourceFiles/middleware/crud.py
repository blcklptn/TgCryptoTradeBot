from database import db
from models.tables import Users, Admins
from datetime import datetime, timedelta
from core import config
from .error_handler import handle_crud_error

session = db.create_database()

async def save(obj: object) -> None:
    session.add(_object)
    session.commit()

@handle_crud_error
async def add_admin(user_id: str) -> None:
    admin: object = Admins(user_id=user_id)
    await save(obj: admin)

@handle_crud_error
async def add_user(username: str, user_id: str) -> None:
    user: object = Users(username=username, user_id=user_id)
    await save(obj: user)

@handle_crud_error
async def add_operator(username: str, user_id: str) -> None:
    operator: object = Operators(username=username, user_id=user_id)
    await save(obj: operator)

