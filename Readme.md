WELCOME TO THE FORMEL DATA PIPELINE

THIS FOLDER INCLUDES A #DATA EXTRACTION# AND #DATA TRANSFORMATION# FOLDER, PLEASE CONTACT THE DEVELOPER IF SOMETHING IS MISSING

### PLEASE FOLLOW THE FOLLOWING STEP BY STEP AS MENTIONED ###

a. First please open the config.json and enter your Big Query Project ID and Dataset ID in the respective Fields
b. Go to your project on Google Cloud and create a new API Key, copy the JSON File contents into 
### client_secret.json 
c. if you would like to provide a new dataset, please replace the data in the 'subscriptions.csv' and 'marketing_spend.csv' files, but please do not change the names of the columns and the overall structure of the file

To execute the Pipeline please execute the following commands in order, please execute these commands from this folder's root, as i have used relative paths, as compared to absolute paths

1. pip install -r requirements.txt
2. python change_sql_file.py
3. python Data_Extraction/data_model.py
4. Create an empty google sheet and name it 'Reports', copy the email from the client_secret.json file and share your google sheet with this email address, please assign 'Editor' rights to this email.
5. python Data_Transformations/transform_and_load.py