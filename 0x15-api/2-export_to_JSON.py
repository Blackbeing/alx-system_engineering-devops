#!/usr/bin/python3

"""
Fetch data from API, export to json
"""

if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    ).json()
    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos"
    ).json()
    user_id = user.get("id", "")

    data = {
        f"{user_id}": [
            {
                "task": todo.get("title", ""),
                "completed": todo.get("completed", ""),
                "username": user.get("username", ""),
            }
            for todo in todos
        ]
    }
    with open(f"{user_id}.json", "w") as fd:
        json.dump(data, fd)
