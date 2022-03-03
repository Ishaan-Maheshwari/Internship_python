from zipfile import ZipFile
import sys
import pandas as pd
import pymongo

zip_filename = 'DGCER.zip'

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["users"]
mycol = mydb["student_data"]

req_header = ['ORG_NAME', 'ORG_NAME_L', 'ORG_ADDRESS', 'ORG_CITY', 'ORG_STATE', 'ORG_PIN', 'ACADEMIC_COURSE_ID', 'COURSE_NAME', 'EXAM_TYPE', 'SESSION', 'REGN_NO', 'RROLL', 'AADHAAR_NO', 'CNAME', 'GENDER', 'DOB', 'FNAME', 'STUDENT_ADDRESS', 'RESULT', 'DIVISION', 'PHOTO', 'MRKS_REC_STATUS', 'YEAR', 'CERT_NO', 'SEM', 'TOT_CREDIT', 'TOT_CREDIT_POINTS', 'GRAND_TOT_MRKS', 'FINAL_GMAX_TOTAL', 'PERCENT', 'CGPA', 'SGPA', 'SUB1NM', 'SUB1', 'SUB1_STATUS', 'SUB1_TH_MRKS', 'SUB1_TH_MAX', 'SUB1_CE_MRKS', 'SUB1_CE_MAX', 'SUB1_PR_MRKS', 'SUB1_PR_MAX', 'SUB2NM', 'SUB2', 'SUB2_STATUS', 'SUB2_TH_MRKS', 'SUB2_TH_MAX', 'SUB2_CE_MRKS', 'SUB2_CE_MAX', 'SUB2_PR_MRKS', 'SUB2_PR_MAX', 'SUB3NM', 'SUB3', 'SUB3_STATUS', 'SUB3_TH_MRKS', 'SUB3_TH_MAX', 'SUB3_CE_MRKS', 'SUB3_CE_MAX', 'SUB3_PR_MRKS', 'SUB3_PR_MAX', 'SUB4NM', 'SUB4', 'SUB4_STATUS', 'SUB4_TH_MRKS', 'SUB4_TH_MAX', 'SUB4_CE_MRKS', 'SUB4_CE_MAX', 'SUB4_PR_MRKS', 'SUB4_PR_MAX', 'Unnamed: 68', 'SUB1MJ', 'SUB1MJ_TYPE', 'SUB2MJ', 'SUB2MJ_TYPE', 'SUB1MN', 'SUB1MN_TYPE', 'SUB2MN', 'SUB2MN_TYPE', 'TOT_CREDIT_HOURS', 'SUB1_CREDIT_HOURS', 'SUB2_CREDIT_HOURS', 'SUB3_CREDIT_HOURS', 'SUB4_CREDIT_HOURS', 'SUB1_GRACE', 'SUB2_GRACE', 'SUB3_GRACE', 'SUB4_GRACE', 'STREAM', 'SUB1_CREDIT_POINTS', 'SUB2_CREDIT_POINTS', 'SUB3_CREDIT_POINTS', 'SUB4_CREDIT_POINTS', 'DOQ', 'DOS', 'DOP', 'DISSERTATION_TITLE', 'CGPA_SCALE', 'STREAM_THIRD', 'STREAM_SECOND', 'SUB_COURSE_NAME', 'GRADE', 'CLASS', 'MONTH']

with ZipFile(zip_filename, 'r', allowZip64 = True) as zip_file:
    csv_file = zip_file.open(name = zip_file.namelist()[-1], mode = 'r')
    dataframe = pd.read_csv(csv_file)
    count = 0
    data_columns = list(dataframe.columns)
    if req_header != data_columns :
        print("ERROR : Columns missing from data :-")
        missing_col = [x for x in req_header if x not in data_columns]
        for col in missing_col:
            print("[Missing Column] ",col)
        sys.exit("ERROR : Incorrect Data")
    else:
        for (row_num, row_data) in dataframe.iterrows():
            x = mycol.insert_one(dict(row_data))
            count = count + 1
        print("Data successfully inserted : ",count)
