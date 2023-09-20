#!/usr/bin/python3
"""Python script that using REST API"""
import requests
import sys

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"

    if len(sys.argv) != 2:
        print("Uso: python script.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]

    user = requests.get(url + "/users/{}".format(user_id)).json()
    todos = requests.get(url + "/todos", params={"userId": user_id}).json()

    total_tasks = len(todos)
    completed_tasks = sum(1 for todo in todos if todo["completed"])

    print("First line: Employee {} is done with tasks ({}/{}):".format(user.get("name"), completed_tasks, total_tasks))

    for todo in todos:
        if todo["completed"]:
            print("\t{}".format(todo["title"]))
