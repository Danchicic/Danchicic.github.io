from .create_db import DataBaseCRUD, User

"""initializing databases"""
DataBase = DataBaseCRUD('../db/comics.db')
UserBase = User()
