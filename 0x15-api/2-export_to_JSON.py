#!/usr/bin/python3

"""Imports a Module"""

import json
import requests
import sys

if len(sys.argv) < 2:
    print("Error: No employee ID provided.")
    sys.exit(1)

try:
    user_id = int(sys.argv[1])
except ValueError:
    print("Error : Employee ID must be an integer.")
    sys.exit(1)

todos_url = 'https://jsonplaceholder.typicode.com/todos'
user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
todos_response = requests.get(todos_url)
user_response = requests.get(user_url)

if todos_response.status_code != 200 or user_response.status_code != 200:
    print(f"Error: Unable to get data for employee with ID {user_id}")
    sys.exit(1)

todos_data = todos_response.json()
user_data = user_response.json()

tasks = []

for todo in todos_data:
    if todo['userId'] == user_id:
        task = {
                'task': todo['title'],
                'completed': todo['completed'],
                'username': user_data['username']

        }
        tasks.append(task)

with open(f'{user_id}.json', 'w') as json_file:
    json.dump({str(user_id): tasks}, json_file)
