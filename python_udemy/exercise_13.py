# I this exercise I have to create a program to open posts from last days from some website in a webbrowser.

import requests
import json
import webbrowser
from datetime import datetime, timedelta

days = int(input('Enter from how many days back posts you want to see. '))
time_today = datetime.today()
time_delta = timedelta(days = days)
date = time_today - time_delta

parameters = {
                'site': 'stackoverflow',
                'sort': 'votes',
                'order': 'desc',
                'fromdate': int(date.timestamp()),
                'tagged': 'python',
                'min': 5
             }

request = requests.get('https://api.stackexchange.com/2.3/questions', parameters)

try:
    questions = request.json()
except json.decoder.JSONDecodeError:
    print('Invalid format.')
else:
    for question in questions['items']:
        webbrowser.open_new_tab(question['link'])
