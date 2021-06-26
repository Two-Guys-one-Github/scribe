""" 
A Scribe that will read and write a SQLite3 database.

SQLite3 DB-API Docs: https://docs.python.org/3/library/sqlite3.htm
"""

from __future__ import annotations
import sqlite3
from sqlite3 import Error
from scribe import Scribe 
from pathlib import Path
from typing import  Union


class Sqlite3_Scribe(Scribe):
    def __init__(self) -> Sqlite3_Scribe:
        super().__init__()
        self.connection = None
        self.db_name = None
        self.db_exists = None  
    def create_connection(self,
                        connection: str, 
                        ) -> Union[sqlite3.Connection, None]:
        """
        Connect to Sqlite3 Database connection from a raw string.
        """
        conn = None
        if connection[-3:] != ".db":
            connection = f"{connection}.db"
        
        db_path = self._format_os_path(connection)
        db_path_exists = Path(Path(db_path).parent).exists()

        if db_path_exists:
            self.db_path = db_path
            self.name = Path(db_path).name
            try:
                conn = sqlite3.connect(self.db_path)
                return conn
            except Error as e:
                print(e)
            return conn
        else:
            raise Exception("Path to Database does not exist.")
        
# testing 
db_path = r"C:\Users\justi\Desktop\scribe\scribe\test_db\sqlite3_sameple.db"
sql_scribe = Sqlite3_Scribe()

# testing -> db_path and db_name
# sql_scribe.create_connection(db_path)
# print(sql_scribe.connection)
# print(sql_scribe.name)

# testing -> Creating connection to nonexisting SQLite3 DB.
conn = sql_scribe.create_connection(db_path)
# print(type(conn))





