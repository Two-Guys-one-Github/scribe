""" 
A Scribe that will read and write a SQLite3 database.

SQLite3 DB-API Docs: https://docs.python.org/3/library/sqlite3.htm
"""

from __future__ import annotations
from scribe.scribe import Scribe
from pathlib import Path
import sqlite3

class Sqlite3_Scribe(Scribe):
    def __init__(self) -> None:
        super().__init__()
        self.connection = None
        self.db_name = None
        


    def create_connection(self,
                        connection: str,  
                        create: bool = True,
                        ):
        """
        Connect to Sqlite3 Database connection from a raw string.
        """
        conn = None
        if create:
            if connection[-3:] != ".db":
                connection = f"{connection}.db"
            self.db_path = self._format_os_path("{connection}")
            self.db_name = Path(self.db_path).name
        
        print(self.db_path)

        #     try:
        #         conn = sqlite3.connect(self.db_path)
            
        # else:
        #     None


        # return None

db_path = r"C:\Users\justi\Desktop\scribe\scribe\test_db"

sql_scribe = Sqlite3_Scribe()

sql_scribe.create_connection(db_path)

    

