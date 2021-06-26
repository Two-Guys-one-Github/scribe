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
        self.tables: Union[list, None] = [] 
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
    def create_new_table(self,
                        conn: sqlite3.Connection,
                        table_name: str,
                        schema: dict,
                        special_schema: str = None, 
                        close_conn: bool = True) -> None:
        
        sql_columns = f""", 
        """.join([f"{i} {j}" for i,j in zip(schema.keys(),
                schema.values())])
        sql_string = f"""CREATE TABLE IF NOT EXISTS {table_name} (
        {sql_columns});"""

        if special_schema != None:                                                 
            pass

        if conn is not None:
            try:
                c = conn.cursor()
                c.execute(sql_string)
            except Error as e:
                print(e)

        if close_conn:
            conn.close()
        return


# test -> db
db_path = r"C:\Users\justi\Desktop\scribe\scribe\test_db\sqlite3_sameple.db"
sql_scribe = Sqlite3_Scribe()


# test -> db_path and db_name report correctly
#conn = sql_scribe.create_connection(db_path)
# sql_scribe.create_connection(db_path)
# print(sql_scribe.connection)
# print(sql_scribe.name)

# test -> Creating connection to nonexisting SQLite3 DB.
conn = sql_scribe.create_connection(db_path)
# print(type(conn))

# Test -> make table schema string is formated correctly
conn = sql_scribe.create_connection(db_path)
table_name = "tbl_test_table"
test_schema = {"type":"text",
               "name":"text",
               "tbl_name":"text",
               "rootpage":"integer",
               "sql":"text",}
sql_scribe.create_new_table(conn,table_name,test_schema)



