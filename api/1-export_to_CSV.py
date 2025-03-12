#!/usr/bin/python3
"""script to get todos"""

import csv
import requests
import sys


def main():
    """main function"""
    employee_id = int(sys.argv[1])

    todos_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    todos_response = requests.get(todos_url)
    todos_response.raise_for_status()
    todos = todos_response.json()

    user_response = requests.get(users_url)
    user_response.raise_for_status()
    user = user_response.json()

    employee_name = user.get("name")

    with open(f"{employee_id}.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "EMPLOYEE_NAME", "COMPLETED", "TITLE"])

        for todo in todos:
            if todo["userId"] == employee_id:
                writer.writerow(
                    [employee_id, employee_name,
                     todo["completed"], todo["title"]]
                )


if __name__ == "__main__":
    main()
