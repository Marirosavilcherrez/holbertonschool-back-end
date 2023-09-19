#!/usr/bin/python3
"""Python script that using REST API"""
import requests
import sys

def give_employee_todo(employee_id):
    "URL API to consult"
    api_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'

    "make a GET request to the API"
    response = requests.get(api_url)

    "check if the request was success"
    if response.status_code == 200:
        todos = response.json()

        "Count the number of completed and total tasks"
        EMPLOYEE_NAME = 'name'
        TASK_TITLE = 'title'
        TOTAL_NUMBER_OF_TASKS = len(todos)
        NUMBER_OF_DONE_TASKS = sum(1 for todo in todos if todo['completed'])

        "print employee TODO list"
        print('Employee {} is done with tasks({}/{}):'\
              .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

        "Print the titles of the completed task"
        for todo in todos:
            if todo['completed']:
                print('\t{}'.format(todo[TASK_TITLE]))
    else:
        print(f'Error: Unable to fetch data for employee {employee_id}')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 script.py <employee_id>")
        sys.exit(1)
    
    userId = int(sys.argv[1])
    give_employee_todo(userId)
