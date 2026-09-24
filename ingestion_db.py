import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

# Logging setup..
logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

# Create a database connection engine using sqlalchemy...
engine = create_engine('sqlite:///inventory.db')

# Function to insert data into database
def ingest_db(df, table_name, engine, if_exists='append'):
    df.to_sql(
        table_name,
          con=engine,
            if_exists=if_exists,
              index=False,
              chunksize=10000
              )


# Function to Load CSV files from the data folder into the database    
def load_raw_data():
    start = time.time()

    for file in os.listdir('data'):
        if file.endswith('.csv'):
            table_name = file[:-4] # Remove the .csv extension to get the table name
            logging.info(f"Ingesting {file} in db")

            first_chunk = True
            for df in pd.read_csv('data/' + file, chunksize=50000):

                logging.info(f"Loading {table_name} with shape {df.shape}")

                if first_chunk:
                 ingest_db(df, table_name, engine, 'replace')
                 first_chunk = False
                else:
                    ingest_db(df, table_name, engine,'append')
    end = time.time()
    total_time = (end - start) / 60

    logging.info("-----Ingestion Completed------")
    logging.info(f"Total Time Taken: {total_time} minutes")

    print("Ingestion Completed")
    print("Total Time Taken:",total_time, "minutes")
if __name__ == "__main__":
    load_raw_data()