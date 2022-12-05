from cmath import nan
import pandas as pd
from modules.Users_Cleanup import create_user
from modules.Subscriptions_Cleanup import create_subscription
from modules.Cancellations_Cleanup import cancellations
from modules.Vouchers_Cleanup import Voucher
from modules.Diagnosis_Cleanup import diagnosis
from modules.Checkin_Cleanup import User_Checkin
from modules.Marketing_Cleanup import Marketing
from modules.raw_file_upload import raw_file
from google.cloud import bigquery
from google.oauth2 import service_account # type: ignore

creds_file_path= "./client_secret.json"

def create_schema():
    """
    Create the database schema by executing the data-model.sql file over Big Query
    """
    credentials = service_account.Credentials.from_service_account_file(
    creds_file_path, scopes=["https://www.googleapis.com/auth/cloud-platform"],
)
    fd = open('../data-model.sql', 'r')
    query = fd.read()
    client = bigquery.Client(credentials = credentials)
    job = client.query(query)
    rows = job.result()
    for val in rows:
        print(val)
        
df=pd.read_csv('./subscriptions.csv')
df=df.drop_duplicates(subset='user_id', keep='first')
df=df.drop_duplicates(subset='subscription_id', keep='first')
create_schema()
print("Users")
create_user(df)
print("Subscriptions")
create_subscription(df)
print("Cancellations")
cancellations(df)
print("Voucher")
Voucher(df)
print("Diagnosis")
diagnosis(df)
print("User Checkin")
User_Checkin(df)
print("Marketing")
Marketing(df)
print("Raw File")
raw_file()
