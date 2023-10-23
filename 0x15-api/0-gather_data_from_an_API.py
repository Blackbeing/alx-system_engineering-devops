#!/usr/bin/python3
"""
Fetch date from API using python requests
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    ).json()
    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos"
    ).json()
    completed = [
        task for task in todos if task.get("completed", False) is True
    ]
    print(
        "Employee {} is done with tasks({}/{}):".format(
            user.get("name", ""), len(completed), len(todos)
        )
    )
    for done in completed:
        print(f"\t {done['title']}")
