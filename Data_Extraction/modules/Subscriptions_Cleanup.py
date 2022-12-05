from cmath import nan
import pandas as pd
import numpy as np
from google.cloud import bigquery
from upload_to_bigquery import load_data_from_file

def create_subscription(df):
    """
    drop columns that are not used, and then cleanup the data by removing nulls and duplicates,
    lastly, upload the data to the database server
    All the other files in this folder function the same way
    """
    to_drop=['age',
            'first_voucher_type',
            'newsletter_subscription',
            'gender',
            'gross_price',
            'diagnosis_condition',
            'diagnosis_severity',
            'ask_your_doctor_count',
            'checkin_date',
            'checkin_score',
            'user_created_date',
            'cancellation_date',
            'lead_time_in_hours',
            'marketing_channel'
            ]
    subscriptions = df.drop(to_drop, axis = 1)
    job_config = bigquery.LoadJobConfig(
    autodetect=True,
    source_format=bigquery.SourceFormat.CSV
    )
    
    load_data_from_file(subscriptions,"Subscriptions", job_config)
