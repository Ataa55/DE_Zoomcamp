import os
import pandas as pd
import sqlalchemy
import argparse
from time import time



def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table = params.table
    url = params.url

    

     

    engine = sqlalchemy.create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}', echo= False)
    
    if url.endswith(".csv.gz"):
        csv_name = "output.csv.gz"

    else:
        csv_name = csv_name = "output.csv"

    #download the csv
    os.system(f"wget {url} -O {csv_name}")
    
    df_iter = pd.read_csv(csv_name, iterator=True, chunksize = 100000)
    df = next(df_iter)


    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    df.head(n=0).to_sql(name =table, index = False, con=engine, if_exists = 'replace')

    df.to_sql(name =table, index = False, con=engine, if_exists = 'append')


    while True:
        start = time()
        
        df = next(df_iter)
        
        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
        
        df.to_sql(name =table, index = False, con=engine, if_exists = 'append')

        end = time()

        print(f"chunk ingetion to the the db took {end - start}")



    


parser = argparse.ArgumentParser(description='ingest csv data into postgress')




if __name__ == '__main__':
    parser.add_argument('--user', required=True, help='user name for postgress')
    parser.add_argument('--password',required=True, help='pass for postgress')
    parser.add_argument('--host', required=True, help='datatbase host')
    parser.add_argument('--port', required=True, help='port for postgress')
    parser.add_argument('--db', required=True, help='name for the database')
    parser.add_argument('--table', required=True, help='table name')
    parser.add_argument('--url', required=True, help='url for the csv')

    args = parser.parse_args()

    main(args)
