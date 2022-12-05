from cmath import nan
import pandas as pd
import numpy as np
from upload_to_bigquery import load_data_from_file
from google.cloud import bigquery

def Marketing(df):
    """
    drop columns that are not used, and then cleanup the data by removing nulls and duplicates,
    lastly, upload the data to the database server
    All the other files in this folder function the same way
    """
    to_drop=['age',
             'first_voucher_type',
            'cancellation_date',
            'newsletter_subscription',
            'gender',
            'subscription_id',
            'subscription_start_date',
            'subscription_end_date',
            'subscription_interval',
            'lead_time_in_hours',
            'user_created_date',
            'purchase_date',
            'first_voucher_type',
            'gross_price',
            'diagnosis_condition',
            'diagnosis_severity',
            'ask_your_doctor_count',
            'checkin_date',
            'checkin_score'
            ]
    marketing = df.drop(to_drop,axis=1)
    marketing = marketing[marketing.marketing_channel.notnull()]
    marketing = marketing.drop_duplicates()
    job_config = bigquery.LoadJobConfig(
    autodetect=True,
    source_format=bigquery.SourceFormat.CSV
    )

    load_data_from_file(marketing,"Marketing", job_config)