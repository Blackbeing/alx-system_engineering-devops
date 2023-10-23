#!/usr/bin/python3
"""
Fetch data from API, export to json
"""

if __name__ == "__main__":
    import json
    import requests

    users = requests.get(
        "https://jsonplaceholder.typicode.com/users/"
    ).json()
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos"
    ).json()

    with open("todo_all_employees.json", "w") as fd:
        data = {
            f"{user.get('id', '')}": [
                {
                    "username": user.get("username", ""),
                    "task": todo.get("title", ""),
                    "completed": todo.get("completed", ""),
                }
                for todo in todos
                if todo.get("userId", "") == user.get("id")
            ]
            for user in users
        }
        json.dump(data, fd)
