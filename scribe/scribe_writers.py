""" 
A Scribe that will read and write a SQLite3 database.

SQLite3 DB-API Docs: https://docs.python.org/3/library/sqlite3.htm
"""
from __future__ import annotations
import sqlite3
from sqlite3 import Error
from scribe import scribe_manager
import csv
from pathlib import Path
from typing import  Union

class Scribe_SQLite_Writer(scribe_manager.Scribe_Manager):
    def __init__(self) -> Scribe_SQLite_Writer:
        super().__init__()
        self.connection = None
        self.db_name = None
        self.db_exists = None
        self.tables: Union[list, None] = [] 
    def create_sqlite_connection(self,
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
            if self.db_name != None:                           # Check if a custom db name was provided in the parent class.
                self.db_name = Path(db_path).name
            try:
                conn = sqlite3.connect(self.db_path)
                return conn
            except Error as e:
                print(e)
            return conn
        else:
            raise Exception("Path to Database does not exist.")
    def create_new_sqlite_table(self,
                                conn: sqlite3.Connection,
                                schema: dict,
                                table_name: str,
                                special_schema: str = None, 
                                close_conn: bool = True) -> None:
        """
        Create a new SQLite3 table when given a 
        minium of a db name, table name and a schema.
        """
        #Format python string into SQLite3 syntax.
        sql_columns = f""",                                              
        """.join([f"{i} {j}" for i,j in zip(schema.keys(),
                schema.values())])
        sql_string = f"""CREATE TABLE IF NOT EXISTS {table_name} (
        {sql_columns});"""

        if conn is not None:
            try:
                c = conn.cursor()
                c.execute(sql_string)
            except Error as e:
                print(e)

        if close_conn:
            conn.close()
        return
    def insert_into_sqlite_table(self,
                                conn: sqlite3.Connection,
                                csv_path: str,
                                table_name: str,
                                table_shape: tuple,
                                delimiter: str
                                ):
        """Insert data into SQLite database"""


        transmit_size = table_shape[0] 
        cur = conn.cursor()

        
        with open(csv_path, newline='', mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = delimiter)
            columns_list = list(next(csv_reader))
            columns = ",".join(columns_list)
            markers = ",".join("?"*len(columns_list))

            while transmit_size > 0:
                row = tuple(next(csv_reader))
                transmit_size -= 1                             
                sql = f"""INSERT INTO {table_name}({columns})
                VALUES({markers});"""
                cur.execute(sql, row)
                    
        conn.commit()
        print("Sussesful transfer")

        return


            
            




       


    


    pass
