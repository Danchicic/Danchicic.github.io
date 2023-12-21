import shutil
import sqlite3
import datetime
import os
from os.path import isfile, join, isdir

import requests


class ComicRow:
    """
    data class for comics data base
    """

    def __init__(self, comics_photo_url=None):
        self.date = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d_%H:%M")
        self.url = comics_photo_url


class UserRow:
    """data class for users database"""

    def __init__(self, telegram_id: int, page: int = 1, comics: str = ''):
        self.tg_id = telegram_id
        self.page = page
        self.comics = comics


class DataBaseCRUD:
    """
    management panel for database using sqllite3 module
    i think pandas more useful
    """

    def __init__(self, db_path: str):
        """initializing connection for db"""
        conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn = conn
        self.cursor = conn.cursor()

    def __str__(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return str(self.cursor.fetchall())

    def __iter__(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return self.cursor

    def create_new_comic(self, name: str, mode: int = 0):

        """creating new comics table
        :argument mode created for api
        """
        self.cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {name} (
                id INTEGER PRIMARY KEY,
                date TEXT,
                picture_id TEXT
                );
            """
        )
        self.conn.commit()
        if mode:
            from pathlib import Path
            Path(f"../comics_files/{name}").mkdir(parents=True, exist_ok=True)

    def write_data(self, table_name: str, *rows: ComicRow, **kwargs):
        """writing row to table_name"""
        for row in rows:
            # checking for a duplicate
            existing = self.cursor.execute(f"SELECT * FROM {table_name}  WHERE picture_id=?", (row.url,)).fetchone()
            if existing is None:
                if kwargs:
                    # if updating database from api
                    picture = requests.get(url=row.url, stream=True)
                    # getting last page of comics
                    file_name = f'{int(getattr(self, "get_last_page")(table_name)) + 1}.jpg'
                    # downloading picture and saving
                    if picture.status_code == 200:
                        with open(f"../comics_files/{table_name}/{file_name}", 'wb+') as f:
                            shutil.copyfileobj(picture.raw, f)

                    self.cursor.execute(
                        f"""INSERT INTO {table_name}
                        VALUES (?, ?, ?)
                        """,
                        (None, row.date, file_name)
                    )
                else:
                    # inserting new line to table
                    self.cursor.execute(
                        f"INSERT INTO {table_name} "
                        f"VALUES (?, ?, ?)",
                        (None, row.date, row.url))
                self.conn.commit()

        return True

    def delete_table(self, table_name: str, mode: int = 0):
        self.cursor.execute(f"""
        DROP TABLE {table_name}
        """)
        self.conn.commit()
        if mode:
            import shutil
            shutil.rmtree(f"../comics_files/{table_name}")

    # returning columns names
    def __get_columns_name(self, name: str) -> list[str]:
        columns_info = self.conn.execute(f'PRAGMA table_info({name});')
        columns: list[str] = []
        for c in columns_info:
            columns.append(c[1])
        return columns

    @staticmethod
    def get_comics_by_name(table_name: tuple[list[str]], page: int = 1) -> str:
        if list == type(table_name):
            table_name = table_name[0][0]
        file_path = f'../comics_files/{table_name}/{page}.jpg'
        return file_path

    @staticmethod
    def append_table_files(mypath):
        # get files from directory
        only_files = [f for f in os.listdir(mypath) if isfile(join(mypath, f))]
        table_name = mypath.split('/')[-1]
        table.create_new_comic(table_name)
        if only_files:
            for file in only_files:
                table.write_data(table_name, ComicRow(file))

    def get_last_page(self, table_name: str):
        self.cursor.execute(
            f"""
            SELECT MAX(id) FROM {table_name};
            """
        )
        last_page = self.cursor.fetchall()[0][0]
        if last_page is not None:
            return last_page
        return 0

    def print_rows(self, name):
        """
        printing table method
        :param name:
        :return:
        """
        self.cursor.execute(
            f"""
            SELECT * FROM {name};
            """
        )

        print(f"TABLE NAME: {name}")
        print(f"COLUMNS: {self.__get_columns_name(name)}")

        for row in self.cursor.fetchall():
            print(row)


class User(DataBaseCRUD):
    """
    user panel management
    """

    def __init__(self):
        # inheritance of properties and methods of the parent class - DataBaseCRUD
        super().__init__('Users.db')

    # updating database with fresh data
    def write_user(self, row: UserRow):
        self.cursor.execute(
            f"""UPDATE Users 
            SET telegram_id='{row.tg_id}', user_comics='{row.comics}', now_page='{row.page}' 
            WHERE telegram_id={row.tg_id}
            """
        )
        self.conn.commit()

    # getting users page
    def get_page(self, tg_id: int):
        self.cursor.execute(f"""
        SELECT now_page FROM Users WHERE telegram_id ={tg_id}
        """)
        return self.cursor.fetchall()

    # getting user comics
    def get_comics(self, tg_id: int):
        self.cursor.execute(f"""
               SELECT user_comics FROM Users WHERE telegram_id ={tg_id}
               """)
        return self.cursor.fetchall()


def create_user():
    """func to create users table"""
    conn = sqlite3.connect('Users.db')
    cursor = conn.cursor()
    conn = conn
    cursor.execute(f"""
               CREATE TABLE IF NOT EXISTS Users (
                   id INTEGER PRIMARY KEY,
                   telegram_id INT UNIQUE,
                   now_page  INT,
                   user_comics TEXT
                    );
               """)
    conn.commit()


if __name__ == '__main__':
    table = DataBaseCRUD('comics.db')
    table.print_rows('biff_to_the_future_6')
