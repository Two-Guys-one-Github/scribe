from src import scribe
import time

# CSV Files
file_path_001 = r"C:\Users\justi\Desktop\scribe\src\test_materials\test_data\large_sample.csv"
file_path_002 = r"C:\Users\justi\Desktop\scribe\src\test_materials\test_data\names.csv"
file_path_003 = r"C:\Users\justi\Desktop\scribe\src\test_materials\test_data\names_new.csv"
file_path_004 = r"C:\Users\justi\Desktop\scribe\src\test_materials\test_datanew_sample.csv"

# Create SQLite Database Here
SQLite_destination = r"C:\Users\justi\Desktop\scribe\src\test_materials\test_dbs"
# Name SQLite Datbase
SQLite_database_name = "test_large_sample"
# Create a table with this name
SQLite_table_name = "large_sample"


fp = file_path_001

def main():

    scrb2 = scribe.Scribe()
    scrb2.convert_csv_to_SQLite3(file_path_001, 
                                SQLite_destination,
                                SQLite_database_name, 
                                SQLite_table_name,
                                delimiter=','
                                )

if __name__ == '__main__':
    main()
    

    