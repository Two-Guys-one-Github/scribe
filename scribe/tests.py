file_path = r"C:\Users\justi\Desktop\scribe\scribe\test_data\large_sample.csv"
scribe = Scribe_Reader()
scribe.read_from_csv(file_path)

print(scribe.columns)
print(scribe.dtypes)
print(scribe.shape)