#!/usr/bin/python3
"""Python script that using REST API"""
import requests
import sys

def give_employee_todo(employee_id):
    "URL API to consult"
    api_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    api_url2 = f'https://jsonplaceholder.typicode.com/users/{employee_id}'

    "make a GET request to the API"
    response = requests.get(api_url)
    response2 = requests.get(api_url2)

    "check if the request was success"
    if response.status_code == 200 and response2.status_code == 200:
        todos = response.json()
        user_data = response2.json()

        "Count the number of completed and total tasks"
        EMPLOYEE_NAME = user_data['name']
        TOTAL_NUMBER_OF_TASKS = len(todos)
        NUMBER_OF_DONE_TASKS = sum(1 for todo in todos if todo['completed'])

        "print employee TODO list"
        print(f'Employee {EMPLOYEE_NAME} is done with tasks ({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):')

        "Print the titles of the completed task"
        for todo in todos:
            if todo['completed']:
                print(f'\t{todo["title"]}')
    else:
        print(f'Error: Unable to fetch data for employee {employee_id}')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 script.py <employee_id>")
        sys.exit(1)
    
    userId = int(sys.argv[1])
    give_employee_todo(userId)
