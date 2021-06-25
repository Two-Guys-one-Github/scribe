"""" A class reader for files that contian a delimeter"""

from __future__ import annotations
import csv
from pathlib import Path
from pathlib import PureWindowsPath
from pathlib import PurePosixPath
from typing import  Union
from .scribe_data_types import is_float, is_int, is_bool
import platform 
# import pyodbc 
# import sys
# import os


class Scribe(object):
    """A scribe class to common to all sub scribe classes."""
    def __init__(self) -> Scribe:
        self.platform: str = platform.system()                      # Operating System (OS).      
        self.version: str = platform.release()                      # OS Version.
        self.current_version: str = platform.release()              # Combined String of OS and OS-Version.
   
    def _format_os_path(self, this_path: str = None) -> str:
        """Return a file path formated corretly from a string."""
        if isinstance(this_path, str):
            if self.platform == "Windows": return PureWindowsPath(this_path)
            else: return PurePosixPath(this_path)
        else:
            return None
    pass

class Scribe_Reader(Scribe):
    """ Represents a scribe reading files or databases"""
    def __init__(self) -> Scribe_Reader:
        super().__init__()
        self.data_path: str = None                                  # Path to file componet
        self.data_directory: str = None
        self.columns = list()
        self.rows = list()
        self.dtypes = dict()
        self.shape = tuple()
        
    def read_from_csv(self,
                        file_path: str=None, 
                        delimiter:str=',',                        # Specify delimeter type.
                        memory: bool = False,                     # Store in custom memory, a built in sqlite db.
                        read_framework: str ="csv_reader",        # Implement other modules in the future.
                        mode: str = 'r',                          # Mode is default to the reader
                        log_time: bool = False,                   # log time 
                        ):
        """Read a file"""
        self.data_path = self._format_os_path(file_path)
        self.data_directory = Path(self.data_path).parent
        row_count = 0
        found_all_data_types = False

        with open(self.data_path, newline='', mode=mode) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = delimiter)
            self.columns = next(csv_reader)
            d_type_len = len(self.columns)
            for colmn in self.columns:
                self.dtypes[colmn] = ""          
            d_types_count = 0
            while not found_all_data_types:
                row = next(csv_reader)
                row_count += 1
                for col_i, row_i in zip(self.columns, row): 
                    if self.dtypes[col_i] == "":
                        if row_i.__contains__(".") and is_float(row_i):
                            self.dtypes[col_i] = "Float"
                            d_types_count += 1 
                        elif not row_i.__contains__(".") and is_int(row_i):
                            self.dtypes[col_i] = "Integer"
                            d_types_count += 1 
                        elif is_bool(row_i):
                            self.dtypes[col_i] = "Boolean"
                            d_types_count += 1 
                        elif len(row_i)>0:
                            self.dtypes[col_i] = "String"
                            d_types_count += 1 
                        else:
                            self.dtypes[col_i] = ""
                if d_types_count == d_type_len:
                    found_all_data_types = True
            for row in csv_reader:
                row_count += 1
        self.shape = (row_count,d_type_len) 
    pass

class Scribe_Writter(Scribe):
    """ Represents a scribe writting to documents or database. """
    def __init__(self)-> Scribe_Writter:
        super().__init__()
    
    pass

 

