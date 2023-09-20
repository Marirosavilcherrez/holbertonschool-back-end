#!/usr/bin/python3
"""Python script that using REST API"""
from requests import get
from sys import argv


if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    todos = response.json()
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    tasks = []
    response2 = get('https://jsonplaceholder.typicode.com/users')
    user_data = response2.json()

    for user in user_data:
        if user.get('id') == int(argv[1]):
            employee_id = user.get('name')

    for todo in todos:
        if todo.get('userId') == int(argv[1]):
            TOTAL_NUMBER_OF_TASKS += 1

            if todo.get('completed') is True:
                NUMBER_OF_DONE_TASKS += 1
                tasks.append(todo.get('title'))

    print(f"Employee {employee_id} is done with tasks("
          f"{NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")

    for task in tasks:
        print("\t {}".format(task))
