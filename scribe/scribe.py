from __future__ import annotations
from pathlib import Path
from scribe.scribe import scribe_readers
from scribe.scribe import scribe_writers
import sys

from typing import  Union

class Scribe(scribe_writers.Scribe_SQLite_Writer,
            scribe_readers.Scribe_File_Reader):
    def __init__(self) -> Scribe:
        super().__init__()

    def convert_csv_to_SQLite3(self,
                                csv_path: str=None,         # Path to .csv     
                                destination: str=None,      # Where to create .db
                                db_name: str=None,          # Database name
                                table_name: str=None,       # table name
                                **kwargs                    # Custom arguments for reader and writter
                                ):
        """Convert .CSV into a database file"""
        # With scribe reader, read a .csv 
        # **kwargs, are used in params in the subclass Scibe_File_Writter
        # **Kwargs Over-write convert_csv_to_db params
                                                                            # Inherits from scribe_readers.Scribe_File_Reader
        self.read_from_csv(csv_path, **kwargs)                              # Inherits from scribe_readers.Scribe_File_Reader
        if db_name != None:
            destination = f"{destination}\{db_name}.db"
            self.db_name = db_name
        conn = self.create_sqlite_connection(destination)                   # Inherits from scribe_writers_Scribe_Scribe_SQLite_Writer
                                                                            # Create connection also creates new db if it does not exist.
        self.create_new_sqlite_table(conn=conn,
                                    schema=self.dtypes,
                                    table_name=f"tbl_{table_name}",
                                    close_conn =False)
        
        """Insert data into SQLite database"""

        table_name=f"tbl_{table_name}"
        self.insert_into_sqlite_table(conn,
                                        csv_path,
                                        table_name,
                                        self.shape,
                                        self.delimiter)
        
        

