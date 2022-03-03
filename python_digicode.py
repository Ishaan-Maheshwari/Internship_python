from zipfile import ZipFile
import sys
import pandas as pd
import pymongo

zip_filename = 'DGCER.zip'

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["users"]
mycol = mydb["student_data"]

with ZipFile(zip_filename, 'r', allowZip64 = True) as zip_file:
    csv_file = zip_file.open(name = zip_file.namelist()[-1], mode = 'r')
    dataframe = pd.read_csv(csv_file)
    for (row_num, row_data) in dataframe.iterrows():
        x = mycol.insert_one(dict(row_data))
        print(x.inserted_id)
    print("Data successfully inserted")
