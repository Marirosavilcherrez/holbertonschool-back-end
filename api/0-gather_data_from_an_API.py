import requests
import sys

if __name__ == "__main__":
<<<<<<< HEAD
=======
    url = "https://jsonplaceholder.typicode.com"
>>>>>>> 0a1e014181ba408befb77ddd9691ec4762822735
    user_id = sys.argv[1]
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    user_url = "https://jsonplaceholder.typicode.com/users/{user_id}"

    response1 = requests.get(todo_url).json()
    response2 = requests.get(user_url).json()

    number_tasks_done = sum(1 for task in response1 if task["completed"])
    total_tasks = len(response1)

<<<<<<< HEAD
    employee_name = response2.get("name")
    task_titles = [task["title"] for task in response1 if task["completed"]]
=======
    print("Employee {} is done with tasks ({}/{}):".format(
          user.get("name"), completed_tasks, total_tasks))
>>>>>>> 0a1e014181ba408befb77ddd9691ec4762822735

    print("Employee {} is done with tasks({}/{})".format(employee_name, number_tasks_done, total_tasks))
    for title in task_titles:
        print(f"\t{title}")
