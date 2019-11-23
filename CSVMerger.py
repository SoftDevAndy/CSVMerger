import pandas
import json
import datetime

# Read config variables 

config = {}

with open('CSVMerger.config', 'r') as outfile:
    config = json.load(outfile)

# Read the files

csv1 = pandas.read_csv(config['IN_FILE_A_LOCATION'])
csv2 = pandas.read_csv(config['IN_FILE_B_LOCATION'])

cols_to_use = csv2.columns.difference(csv1.columns)

merged = pandas.concat([csv1, csv2[cols_to_use]], axis=1, join='outer').sort_index()
merged.set_index(config['MERGE_COLUMN'], inplace=True)

filename = config['OUT_FOLDER_LOCATION'] + config['OUT_FILENAME'] + "-" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + config['OUTFILE_TYPE']

merged.to_csv(filename, index=False)