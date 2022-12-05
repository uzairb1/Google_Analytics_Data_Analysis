from cmath import nan
import pandas as pd
import numpy as np

from google.cloud import bigquery
from upload_to_bigquery import load_data_from_file

def cancellations(df):
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
            'subscription_id',
            'purchase_date',
            'subscription_start_date',
            'subscription_end_date',
            'subscription_interval',
            'ask_your_doctor_count',
            'checkin_date',
            'checkin_score',
            'user_created_date',
            'marketing_channel'
            ]
    cancellations = df.drop(to_drop, axis = 1)
    cancellations = cancellations[cancellations.cancellation_date.notnull()]
    cancellations = cancellations.drop_duplicates()
    job_config = bigquery.LoadJobConfig(
    autodetect=True,
    source_format=bigquery.SourceFormat.CSV
    )
    
    load_data_from_file(cancellations,"Cancellations", job_config)