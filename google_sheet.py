
from datetime import datetime
from pprint import pprint

import apiclient.discovery
import httplib2
from oauth2client.service_account import ServiceAccountCredentials


class SpreadSheet:

    def __init__(self, credentials_file: str, spreadsheet_id: str):
        self.spreadsheet_id = spreadsheet_id

        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            credentials_file, [
                'https://www.googleapis.com/auth/spreadsheets',
                'https://www.googleapis.com/auth/drive'
            ])
        httpAuth = credentials.authorize(httplib2.Http())

        self.service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

    def view(self):
        values = self.service.spreadsheets().values().get(
            spreadsheetId=self.spreadsheet_id,
            range='Дашборд!B2',
            majorDimension='COLUMNS'
        ).execute()
        pprint(values)

    def update(self):
        self.service.spreadsheets().values().batchUpdate(
            spreadsheetId=self.spreadsheet_id,
            body={
                "valueInputOption": "USER_ENTERED",
                "data": [
                    {
                        "range": "Повседневные!A2:D2",
                        "majorDimension": "ROWS",
                        "values": [
                            [datetime.now().strftime('%d.%m.%Y'),
                             "Продукты", 100, ""]
                        ]
                    }
                ]
            }
        ).execute()

    def append(self, category: str, amount: int, comment: str = ''):
        self.service.spreadsheets().values().append(
            spreadsheetId=self.spreadsheet_id,
            range="Повседневные!A:D",
            valueInputOption="USER_ENTERED",
            insertDataOption="OVERWRITE",
            body={
                "majorDimension": "ROWS",
                "values": [
                    [datetime.now().strftime('%d.%m.%Y'), category, amount, comment]
                ]
            }
        ).execute()
