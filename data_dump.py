import pymongo
import pandas as pd
import json

client =   pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

database_name = "aps"
collection_name = "sensor"
data_file_path = "/config/workspace/aps_failure_training_set1.csv"

if __name__=="__main__":
    df = pd.read_csv(data_file_path)
    print(f"rows and col :{df.shape}")

    #covert DF to JSON
    df.reset_index(drop=True,inplace=True)
    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    #insert data to mongo db
    client[database_name][collection_name].insert_many(json_record)

