import sqlite3
import datetime
import os
from os.path import isfile, join, isdir


class ComicRow:
    def __init__(self, comics_photo_url=None):
        self.date = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d_%H:%M")
        self.url = comics_photo_url


class UserRow:
    def __init__(self, telegram_id: int, page: int = 1, comics: str = ''):
        self.tg_id = telegram_id
        self.page = page
        self.comics = comics


class DataBaseCRUD:
    # def __new__(cls):
    #     if not hasattr(cls, 'instance'):
    #         cls.instance = super(DataBaseCRUD, cls).__new__(cls)
    #     return cls.instance

    def __init__(self, db_path: str):
        """initializing connection for db"""
        conn = sqlite3.connect(db_path)
        self.cursor = conn.cursor()
        self.conn = conn

    def __str__(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return str(self.cursor.fetchall())

    def __iter__(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        # print(self.cursor.fetchall())
        return self.cursor

    def create_new_comic(self, name: str):
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

    def write_data(self, table_name: str, *rows: ComicRow):
        for row in rows:
            self.cursor.execute(
                f"INSERT OR IGNORE INTO {table_name} "
                f"VALUES (?, ?, ?) ",
                (None, row.date, row.url))
        self.conn.commit()

    def _get_columns_name(self, name: str) -> list[str]:
        columns_info = self.conn.execute(f'PRAGMA table_info({name});')
        columns: list[str] = []
        for c in columns_info:
            columns.append(c[1])
        return columns

    def get_comics_by_name(self, table_name: tuple[list[str]], page: int = 1) -> str:
        "../comics_files/biff_to_the_future_1/7.jpg"
        if list == type(table_name):
            table_name = table_name[0][0]

        file_path = f'../comics_files/{table_name}/{page}.jpg'
        return file_path

    def get_last_page(self, table_name: str):
        self.cursor.execute(
            f"""
            SELECT 
            """
        )
        pass

    def print_rows(self, name):
        self.cursor.execute(
            f"""
            SELECT * FROM {name};
            """
        )

        print(f"TABLE NAME: {name}")
        print(f"COLUMNS: {self._get_columns_name(name)}")

        for row in self.cursor.fetchall():
            print(row)
        # print(self.cursor.fetchall())


def append_table_files(mypath, table_name):
    onlyfiles = [f for f in os.listdir(mypath) if isfile(join(mypath, f))]
    table.create_new_comic(table_name)
    if onlyfiles:
        for file in onlyfiles:
            table.write_data(table_name, ComicRow(file))
    else:
        table_names = []
        directories = [f"{mypath}/{f}" for f in os.listdir(mypath) if isdir(join(mypath, f))]
        for dr in directories:
            table_name = '_'.join(dr.split('/')[-2::])
            table.create_new_comic(table_name)
            for f in os.listdir(dr):
                if isfile(join(dr, f)):
                    table.write_data(table_name, ComicRow(f"{dr}/{f}"))
            table_names.append(table_name)
        return table_names


class User(DataBaseCRUD):

    def __init__(self):
        super().__init__('../db/Users.db')

    def write_user(self, row: UserRow):
        self.cursor.execute(
            f"""UPDATE Users 
            SET telegram_id='{row.tg_id}', user_comics='{row.comics}', now_page='{row.page}' 
            WHERE telegram_id={row.tg_id}
            """
        )
        self.conn.commit()

    def get_page(self, tg_id: int):
        self.cursor.execute(f"""
        SELECT now_page FROM Users WHERE telegram_id ={tg_id}
        """)
        return self.cursor.fetchall()

    def get_comics(self, tg_id: int):
        self.cursor.execute(f"""
               SELECT user_comics FROM Users WHERE telegram_id ={tg_id}
               """)
        # print(self.cursor.fetchall())
        return self.cursor.fetchall()


def create_user():
    conn = sqlite3.connect('../db/Users.db')
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
    table = DataBaseCRUD('../db/comics.db')
    table.create_new_comic("PeppaPig")
    table.create_new_comic("Cyberpunk_Edgerunners_Rebecca")
