# I this exercise I have to create a program to check which website from file which I will upload in future is working and which not. 

import requests

opened_file = input('Enter the name of the file to open. (With extension!)')

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False

with open(opened_file, 'r') as file:
    for line in file:
        url = line.strip()
        if check_website(url):
            print(f'{url} is up and running')
        else:
            print(f'{url} is down')

# It works but I have no idea why third website is as a "down" because it exist and works well in real. 