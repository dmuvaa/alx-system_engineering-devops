#!/usr/bin/python3

"""Imports a Module"""

import csv
import requests
import sys


def main():
    """Main Function of the API"""
    if len(sys.argv) < 2:
        print("Error: No employee ID provided.")
        sys.exit(1)

    try:
        user_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    todos_response = requests.get(todos_url)
    user_response = requests.get(user_url)

    if todos_response.status_code != 200 or user_response.status_code != 200:
        print(f"Error: Unable to get data for employee with ID {user_id}")
        return

    todos_data = todos_response.json()
    user_data = user_response.json()

    with open(f'{user_id}.csv', 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME',
                      'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)

        for todo in todos_data:
            if todo['userId'] == user_id:
                writer.writerow({'USER_ID': user_id,
                                 'USERNAME': user_data['username']
                                 'TASK_COMPLETED_STATUS': todo['completed'],
                                 'TASK_TITLE': todo['title']})


if __name__ == '__main__':
    """call main"""
    main()
