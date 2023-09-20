#!/usr/bin/python3
"""Python script that using REST API"""
import requests
import sys

def fetch_user_data(user_id):
    try:
        url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
        response = requests.get(url)
        response.raise_for_status()

        user_data = response.json()
        return user_data
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener datos del usuario: {e}")
        sys.exit(1)

def fetch_user_todos(user_id):
    try:
        url = "https://jsonplaceholder.typicode.com/todos"
        params = {"userId": user_id}
        response = requests.get(url, params=params)
        response.raise_for_status()

        todos = response.json()
        return todos
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener las tareas del usuario: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]

    user_data = fetch_user_data(user_id)
    todos = fetch_user_todos(user_id)

    total_tasks = len(todos)
    completed_tasks = sum(1 for todo in todos if todo["completed"])

    print(f"Empleado {user_data.get('name')} ha completado tareas ({completed_tasks}/{total_tasks}):")

    for todo in todos:
        if todo["completed"]:
            print(f"\t {todo['title']}")
