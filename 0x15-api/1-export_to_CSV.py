#!/usr/bin/python3
"""
Fetch data from API using requests format to csv
"""

if __name__ == "__main__":
    from csv import writer, QUOTE_ALL
    import requests
    from sys import argv

    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    ).json()
    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos"
    ).json()
    user_id = user.get("id", "")

    with open(f"{user_id}.csv", "w", newline="") as fd:
        writer = writer(fd, quotechar='"', quoting=QUOTE_ALL)
        for todo in todos:
            data = [
                user_id,
                user.get("username", ""),
                todo.get("completed", ""),
                todo.get("title", ""),
            ]
            writer.writerow(data)
