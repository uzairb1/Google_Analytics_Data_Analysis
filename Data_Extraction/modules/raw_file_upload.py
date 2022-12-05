import pandas as pd
from google.cloud import bigquery
from upload_to_bigquery import load_data_from_file
def raw_file():
    """
    upload the raw files to big query as well, for the purpose of a few queries
    """
    df = pd.read_csv("./marketing_spend.csv")
    df1 = pd.read_csv("./subscriptions.csv")

    job_config = bigquery.LoadJobConfig(
    autodetect=True,
    source_format=bigquery.SourceFormat.CSV
    )

    load_data_from_file(df,"formel_marketing", job_config)
    load_data_from_file(df1,"formel_subscriptions", job_config)