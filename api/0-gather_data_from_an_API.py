#!/usr/bin/python3
"""script to get todos"""

import requests
import sys


def main():
    """main function"""
    employeeID = int(sys.argv[1])
    
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = f"https://jsonplaceholder.typicode.com/users/{employeeID}"

    todos_response = requests.get(todos_url)
    todos_response.raise_for_status()
    todos = todos_response.json()

    user_response = requests.get(users_url)
    user_response.raise_for_status()
    user = user_response.json()

    EMPLOYEE_NAME = user.get("name")
    TOTAL_NUMBER_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = 0
    titles = []

    for todo in todos:
        if todo.get("userId") == employeeID:
            TOTAL_NUMBER_OF_TASKS += 1
            if todo.get("completed"):
                titles.append(todo.get("title"))
                NUMBER_OF_DONE_TASKS += 1

    print(
        f"Employee {EMPLOYEE_NAME} is done with tasks"
        f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):"
    )
    for title in titles:
        print("\t " + title)


if __name__ == "__main__":
    main()
