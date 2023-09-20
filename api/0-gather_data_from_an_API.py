#!/usr/bin/python3
"""Python script that using REST API"""
from requests import get
from sys import argv


if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    todos = response.json()
    number_tasks = 0
    total_tasks = 0
    tasks = []
    response2 = get('https://jsonplaceholder.typicode.com/users')
    user_data = response2.json()

    for user in user_data:
        if user.get("id") == int(argv[1]):
            employee_id = user.get("name")

    for todo in todos:
        if todo.get("userId") == int(argv[1]):
            total_tasks += 1

            if todo.get('completed') is True:
                number_tasks += 1
                tasks.append(todo.get("title"))

    print(f"Employee {employee_id} is done with tasks("
          f"{number_tasks}/{total_tasks}):")

    for task in tasks:
        print("\t {}".format(task))
