
from datetime import datetime
from time import time

import apiclient
import httplib2
import pytz
from oauth2client.service_account import ServiceAccountCredentials


class SpreadSheet:

    def __init__(self, credentials_file: str, spreadsheet_id: str):
        self.spreadsheet_id = spreadsheet_id
        self.tz = pytz.timezone('Europe/Moscow')

        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            credentials_file, [
                'https://www.googleapis.com/auth/spreadsheets',
                'https://www.googleapis.com/auth/drive'
            ])
        httpAuth = credentials.authorize(httplib2.Http())

        self.service = apiclient.discovery.build(
            'sheets', 'v4', http=httpAuth, cache_discovery=False)

    def view(self):
        values = self.service.spreadsheets().values().batchGet(
            spreadsheetId=self.spreadsheet_id,
            ranges=['Дашборд!B2', 'Дашборд!E4:E5',
                    'Дашборд!J4:J6', 'Дашборд!L4'],
            majorDimension='ROWS'
        ).execute()

        texts = [
            'Статус:',
            'Последние расходы внесены:',
            'Средний расход за текущий месяц:',
            'Повседневные:',
            'Крупные:',
            'Квартира:',
            'Всего потрачено за весь период учета расходов:'
        ]

        list_values = []

        for ranges in values['valueRanges']:
            for r in ranges['values']:
                list_values.append(r[0].replace('\xa0', ' '))

        return [' '.join(x) for x in zip(texts, list_values)]

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
                    [datetime.now(self.tz).strftime('%d.%m.%Y'),
                     category, amount, comment]
                ]
            }
        ).execute()


class Calendar:

    def __init__(self, credentials_file: str):
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            credentials_file, [
                'https://www.googleapis.com/auth/calendar'
            ])
        httpAuth = credentials.authorize(httplib2.Http())

        self.service = apiclient.discovery.build(
            'calendar', 'v3', http=httpAuth, cache_discovery=False)

    def view(self):
        now = datetime.utcnow().isoformat() + 'Z'
        now_1day = round(time())+86400  # плюс сутки
        now_1day = datetime.fromtimestamp(now_1day).isoformat() + 'Z'

        events_result = self.service.events().list(calendarId='gdemoinap@gmail.com', timeMin=now, timeMax=now_1day,
                                                   maxResults=50, singleEvents=True,
                                                   orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])
