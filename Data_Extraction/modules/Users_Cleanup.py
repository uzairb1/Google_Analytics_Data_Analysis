from cmath import nan
import pandas as pd
import numpy as np
from upload_to_bigquery import load_data_from_file
from google.cloud import bigquery

def has_voucher(row):
    """
    marks null values from the voucher column as False, the rest is marke as True
    """
    if row['first_voucher_type'] == '':
        val = False
    else:
        val = True
    return val
def create_user(df):
    """
    drop columns that are not used, and then cleanup the data by removing nulls and duplicates,
    lastly, upload the data to the database server
    """
    to_drop=['purchase_date',
            'subscription_start_date',
            'subscription_end_date',
            'subscription_interval',
            'lead_time_in_hours',
            'gross_price',
            'diagnosis_condition',
            'diagnosis_severity',
            'ask_your_doctor_count',
            'checkin_date',
            'checkin_score',
            'marketing_channel'
            ]
    user=df.drop(to_drop, axis=1)
    user.loc[user['first_voucher_type'].notnull(), 'first_voucher_type'] = True
    user.loc[user['cancellation_date'].notnull(), 'cancellation_date'] = True
    user['first_voucher_type']=user['first_voucher_type'].replace(np.nan, False)
    user['cancellation_date']=user['cancellation_date'].replace(np.nan, False)
    user.rename({'first_voucher_type':'has_voucher','cancellation_date':'is_active'}, axis=1, inplace=True)
    user=user.drop_duplicates()
    #user.to_csv('csvs/Users.csv')
    job_config = bigquery.LoadJobConfig(
    autodetect=True,
    source_format=bigquery.SourceFormat.CSV
    )

    load_data_from_file(user,"Users", job_config)
