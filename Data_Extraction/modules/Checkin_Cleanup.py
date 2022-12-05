from cmath import nan
import pandas as pd
import numpy as np
from google.cloud import bigquery
from upload_to_bigquery import load_data_from_file


def User_Checkin(df):
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
            'checkin_score',
            'marketing_channel'
            ]
    checkin = df.drop(to_drop,axis=1)
    checkin = checkin[checkin.checkin_date.notnull()]
    checkin = checkin.drop_duplicates()
    job_config = bigquery.LoadJobConfig(
    autodetect=True,
    source_format=bigquery.SourceFormat.CSV
    )

    load_data_from_file(checkin,"Check-IN", job_config)
