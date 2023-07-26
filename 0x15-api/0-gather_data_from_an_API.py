#!/usr/bin/python3

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

    total_tasks = 0
    compiled_tasks = []

    for todo in todos.data:
        if todo['user_Id'] == user_id:
            total_tasks += 1

            if todo['completed']:
                completed_tasks.append(todo['title'])

    print(f"Employee {user_data['name']} is done with tasks
          ({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")

if __name__ == '__main__':
    main()
