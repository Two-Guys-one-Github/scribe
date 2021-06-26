"""" 
A class reader for reading in...

1. files that contian a delimeter (.csv and .tsv).
2. files with no delimeter (.txt , .pdf, .html).
3. Static Images (.png, .jpeg, .tif)
4. Datbase tables from...
    4a.     SQLite3 (LAN)
    4b.     Postgress (LAN, AWS?)
    4c.     Microsoft SQL SERVER (LAN, AZURE?)
    4d.     MySql (LAN, AWS?)
    4e.     Custom Connect Script or API, with a custom Json or XML responce format.
"""

from __future__ import annotations
import csv
from . import scribe_manager
from pathlib import Path
from pathlib import PureWindowsPath
from pathlib import PurePosixPath
from typing import  Union, Dict

class Scribe_File_Reader(scribe_manager.Scribe_Manager):
    """ Represents a scribe reading files or databases"""
    def __init__(self) -> Scribe_File_Reader:
        super().__init__()
        self.data_path: Union[str,None] = None                     # Path to file componet
        self.data_directory: Union[str,None] = None
        self.columns: Union[list,None] = None
        self.rows: Union[list,None] = None
        self.dtypes: Union[Dict,None] = None
        self.shape: Union[tuple,None] = None

    def read_from_csv(self,
                        file_path: str=None, 
                        delimiter:str=',',                        # Specify delimeter type.
                        memory: bool = False,                     # Store in custom memory, a built in sqlite db.
                        read_framework: str ="csv_reader",        # Implement other modules in the future.
                        mode: str = 'r',                          # Mode is default to the reader
                        log_time: bool = False,                   # log time 
                        ):
        """Read a csv file"""
        self.data_path = self._format_os_path(file_path)
        self.data_directory = Path(self.data_path).parent
        row_count = 0
        found_all_data_types = False
        self.dtypes = {}

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
                        self.dtypes[col_i] = self.str_is_type(row_i)
                        d_types_count += 1
                if d_types_count == d_type_len:
                    found_all_data_types = True

            for row in csv_reader:
                row_count += 1 
    pass
file_path_001 = r"C:\Users\justi\Desktop\scribe\scribe\test_materials\test_data\large_sample.csv"
# Test Scribe_Reader.read_from_csv()
def test_scribe_file_Reader_001(file_path):
    scribe = Scribe_File_Reader()
    scribe.read_from_csv(file_path)
    print(scribe.columns)
    print(scribe.dtypes)
    print(scribe.shape)