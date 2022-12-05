import pandas as pd
import numpy as np
from google.cloud import bigquery
from google.oauth2 import service_account # type: ignore
import sys

creds_file_path = "./client_secret.json"

def load_data_from_file(df,table_name, job_config):
    """
    truncates the existing table and loads the new data to Big Query Tables
    """
    credentials = service_account.Credentials.from_service_account_file(
    creds_file_path, scopes=["https://www.googleapis.com/auth/cloud-platform"],
    )
    try:
        client = bigquery.Client(credentials=credentials, project=credentials.project_id,)
        project_id="my-project-1535534415901."
        user = "formel_Uzi."
        table_id = project_id+user+table_name
        query = "truncate table `"+table_id+"`"
        query_job = client.query(query)
        for row in query_job:
            print(row)
        print("successfully truncated!!")

        # Since string columns use the "object" dtype, pass in a (partial) schema
        # to ensure the correct BigQuery data type.
        

        job = client.load_table_from_dataframe(
            df, table_id, job_config=job_config
        )

        # Wait for the load job to complete. (I omit this step)
        print("Upload Job Created Successfully")
        print(job.result())  
    except Exception as e:
        print(str(e))
        sys.exit(1)
