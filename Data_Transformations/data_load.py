
import gspread # type: ignore
from oauth2client.service_account import ServiceAccountCredentials # type: ignore
import csv

def upload(file_name):
        """
        This is the loading for transformations, it takes the CSV files from the Result Set Folder 
        and uploads the files to Google Sheets to be used by the Google Data Studio 
        """
        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
                "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

        credentials = ServiceAccountCredentials.from_json_keyfile_name('./client_secret.json', scope)
        client = gspread.authorize(credentials)

        file='Data_Transformations/Result_Sets/'+file_name+'.csv'
        spreadsheet = client.open('Reports')
        spreadsheetId=spreadsheet.id
        sh = client.open_by_key(spreadsheetId)
        sh.values_update(
        file_name,
        params={'valueInputOption': 'USER_ENTERED'},
        body={'values': list(csv.reader(open(file)))}
        )
        print('saved to google sheet')