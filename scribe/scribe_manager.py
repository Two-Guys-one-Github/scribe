"""
A scribe manager class of its subclasses (Read & Write).
Scribe will handle the following...

1. operating systems.
2. Translanting data types / schema's.
3. Manage logs.
4. Manage backups.
5. Manage Timezones.
6. TBD 
"""
from __future__ import annotations
from pathlib import Path
from pathlib import PureWindowsPath
from pathlib import PurePosixPath
from typing import  Union, Dict
import platform
import re

class Scribe_Manager(object):
    """A scribe class to common to all sub scribe classes."""
    def __init__(self) -> Scribe_Manager:
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
    
    def str_is_type(self, data: Union[str, None], whos_dtypes: str = "SQLite3") -> str:
        """"Return the type of data from a string"""
        if whos_dtypes == "SQLite3":
            if data.__contains__("."):
                try:
                    val = float(data)
                    return "REAL"
                except ValueError:
                    pass
            try:
                val = int(data)
                return "INTEGER"
            except ValueError:
                if data == "True":
                    return "BOOLEAN"
                elif data == "False":
                    return "BOOLEAN"
                elif len(data) == 0:
                    return "NULL"
                elif data == " ":
                    return "NULL"
                else:
                    return "TEXT"
        return "Nan"



                
                
                
                
        
    # def str_is_type(self, data: Union[str, None]) -> str:
    #     """"Return the type of data from a string"""
    #     if (re.search(r'[+-]?[0-9]+\.[0-9]+', data)):
    #         try:
    #             val = float(data)
    #             return "float"
    #         except ValueError:
    #             return "str"
    #     else:
    #         try:
    #             val = int(data)
    #             return "int"
    #         except ValueError:
    #             pass
    #     if data == "True" or "False":
    #         return "bool"
    #     elif data == "" or data == None:
    #         return "None_1"
    #     elif len(data) > 0:
    #         return "str"
    #     else:
    #         return "None_2"
    
    