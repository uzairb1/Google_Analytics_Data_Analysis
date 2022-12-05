from cmath import nan
import pandas as pd
import numpy as np
from upload_to_bigquery import load_data_from_file
from google.cloud import bigquery

def Voucher(df):
    """
    drop columns that are not used, and then cleanup the data by removing nulls and duplicates,
    lastly, upload the data to the database server
    All the other files in this folder function the same way
    """
    to_drop=['age',
            'cancellation_date',
            'newsletter_subscription',
            'gender',
            'gross_price',
            'diagnosis_condition',
            'diagnosis_severity',
            'subscription_id',
            'subscription_start_date',
            'subscription_end_date',
            'subscription_interval',
            'lead_time_in_hours',
            'ask_your_doctor_count',
            'checkin_date',
            'checkin_score',
            'user_created_date',
            'purchase_date',
            'marketing_channel'
            ]
    vouchers = df.drop(to_drop, axis=1)
    vouchers = vouchers[vouchers.first_voucher_type.notnull()]
    vouchers = vouchers.drop_duplicates()
    job_config = bigquery.LoadJobConfig(
    autodetect=True,
    source_format=bigquery.SourceFormat.CSV
    )

    load_data_from_file(vouchers,"Voucher", job_config)
