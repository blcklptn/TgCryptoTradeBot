from database import db
from models.tables import Users
from datetime import datetime, timedelta
from core import config

session = db.create_database()

class ManageUsers:

    def set_default_admin(self) -> None:
        try:
            users = Users(user_id='123', role='admin', username='blcklptn')
            session.add(users)
            session.commit()
        except Exception as ex:
            print('Error', ex)
    