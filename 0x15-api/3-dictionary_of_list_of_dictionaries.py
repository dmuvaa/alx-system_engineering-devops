#!/usr/bin/python3

"""Imports Json, Requests, and Sys Libraries"""

import json
import requests


users_url = 'https://jsonplaceholder.typicode.com/users'
users_response = requests.get(users_url)

if users_response.status_code != 200:
    print(f"Error: Unable to get user data")
    sys.exit(1)

users_data = users_response.json()
tasks_dict = {}

for user in users_data:
    user_id = user['id']
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    todos_response = requests.get(todos_url)

    if todos_response.status_code != 200:
        print(f"Error: Unable to get tasks for user ID {user_id}")
        continue

    todos_data = todos_response.json()
    tasks = []

    for todo in todos_data:
        if todo['userId'] == user['id']:
            task = {
                    'task': todo['title'],
                    'completed': todo['completed'],
                    'username': user['username']
            }
            tasks.append(task)

    tasks_dict[str(user_id)] = tasks

with open('todo_all_employees.json', 'w') as json_file:
    json.dump(tasks_dict, json_file)
