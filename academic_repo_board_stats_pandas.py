import pandas as pd
import config
from pymongo import MongoClient
from datetime import datetime


class BoardsData:

    def __init__(self):
        self.collections = config.collections
        self.client = MongoClient(config.mongo_uri)
        self.db = self.client[config.db]        
        self.stats_collection = self.db["academic_repo_board_stats"]
   
    def fetch_boards(self):
        records = []
        response_code = 200
        ResponseMessage = 'success'
        response = {}
        start_time = datetime.now()
        start_time_format = start_time.strftime("%d-%m-%Y %H:%M:%S")
        insert_date = start_time.strftime("%Y-%m-%d")
        
        isExist = self.stats_collection.count_documents({"insert_date" : insert_date})
        if isExist > 0 :
            self.stats_collection.delete_many({"insert_date":insert_date})
        
        if self.collections:
            for collection in self.collections:
                data = pd.DataFrame(list(self.db[collection].find()))
                uri = list(data["URI"])
                if type(uri[0]) == type({}):
                    doc_type = (list(uri[0].keys())[0])
                else:
                    doc_type = uri[0].split('-')[1]
                year_wise_data = dict((data.groupby("YEAR")['_id'].count()))
                for key in year_wise_data.keys() :
                    record_data = {}
                    record_data['board'] = collection
                    record_data['doc-type'] = doc_type
                    record_data['year'] = str(key)
                    record_data['state_code'] = collection[:2]
                    record_data['total_count'] = str(year_wise_data[key])
                    start_time = datetime.now()
                    record_data['insert_at'] = start_time.strftime("%d-%m-%Y %H:%M:%S")
                    record_data['insert_date'] = start_time.strftime("%Y-%m-%d") 
                    records.append(record_data)

        try :
            if len(records) > 0 :
                for i in records:
                    self.stats_collection.insert_one(i)                
        except Exception  as ExceptionError:
            response_code = 300
            ResponseMessage = str(ExceptionError)            
             
        response.update( {'ResponseStatusCode' : response_code} )
        response.update( {'ResponseMessage' : ResponseMessage} )   
        print(response) 
boards = BoardsData()
boards.fetch_boards()
