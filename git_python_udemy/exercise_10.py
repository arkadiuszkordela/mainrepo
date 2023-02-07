# In this exercise I have to make a program which will show me what users from a site completed most of a tasks.

import requests

response = requests.get('https://jsonplaceholder.typicode.com/todos')

todos = response.json()

task_count = {}

for todo in todos:
    if todo['completed']:
        if todo['userId'] in task_count:
            task_count[todo['userId']] += 1
        else:
            task_count[todo['userId']] = 1

most_tasks = max(task_count, key=task_count.get)

# Print the results
print(f'User {most_tasks} completed the most tasks ({task_count[most_tasks]} tasks).')
