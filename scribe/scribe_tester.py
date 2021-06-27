import scribe
import time

file_path_001 = r"C:\Users\justi\Desktop\scribe2\test_materials\test_data\large_sample.csv"
file_path_002 = r"C:\Users\justi\Desktop\scribe2\test_materials\test_data\names.csv"
file_path_003 = r"C:\Users\justi\Desktop\scribe2\test_materials\test_data\names_new.csv"
file_path_004 = r"C:\Users\justi\Desktop\scribe2\test_materials\test_data\new_sample.csv"

destination = r"C:\Users\justi\Desktop\scribe2\test_materials\test_dbs"
database_name1 = "names_new_db"
table_name1 = "names"

database_name2 = "large_sample_db"
table_name2 = "samples"


fp = file_path_001

def main():

    # scrb1 = scribe.Scribe()
    # scrb1.convert_csv_to_SQLite3(file_path_003, 
    #                             destination,
    #                             database_name1, 
    #                             table_name1,
    #                             delimiter=','
    #                             )
  
    scrb2 = scribe.Scribe()
    scrb2.convert_csv_to_SQLite3(file_path_001, 
                                destination,
                                database_name2, 
                                table_name2,
                                delimiter=','
                                )




if __name__ == '__main__':
    main()
    

    