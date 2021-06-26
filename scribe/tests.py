from . import scribe_reader


file_path_001 = r"C:\Users\justi\Desktop\scribe\scribe\tests\test_data\large_sample.csv"
file_path_002 = r"C:\Users\justi\Desktop\scribe\scribe\tests\test_data\names.csv"
file_path_002 = r"C:\Users\justi\Desktop\scribe\scribe\tests\test_data\new_names.csv"
                  
# Test Scribe_Reader.read_from_csv()
def test_scribe_file_Reader_001(file_path):
    scribe = scribe_reader.Scribe_File_Reader()
    scribe.read_from_csv(file_path)
    print(scribe.columns)
    print(scribe.dtypes)
    print(scribe.shape)