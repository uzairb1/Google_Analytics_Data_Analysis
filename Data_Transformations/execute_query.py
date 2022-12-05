import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account # type: ignore
import sys
from os import walk

def execute_query(query_name):
    """
    This function takes in a table name as the argument and then creates a query to be
    executed on Big Query
    """
    credentials = service_account.Credentials.from_service_account_file(
    "./client_secret.json", scopes=["https://www.googleapis.com/auth/cloud-platform"],
    )
    try:
        bqclient = bigquery.Client(credentials=credentials, project=credentials.project_id,)
        query_file = open('Data_Transformations/Queries/'+query_name+'.sql', 'r')
        query_string = query_file.read()
        #print(query_string)
        query_file.close()
        dataframe = (
        bqclient.query(query_string)
        .result()
        .to_dataframe(
            create_bqstorage_client=True,
        )
        )
        dataframe.to_csv('Data_Transformations/Result_Sets/'+query_name+'.csv')
        print(query_name+' successfully executed, results stored in the Result_Sets folder')
    except Exception as e:
        print(str(e))
        sys.exit(1)
