#!/usr/bin/python3
""""
 A python script that exports data in Json format.
 Requirements:
    Records all tasks from all employees
    Format must be: { "USER_ID": [ {"username": "USERNAME", "task":
    "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
    {"username": "USERNAME", "task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS}, ... ],
    "USER_ID":[ {"username": "USERNAME", "task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME",
    "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
    File name must be: todo_all_employees.json
 """

import json
import requests
import sys


def fetch_all_user():
    """Fetch all users' information and to-do lists for employees. """
    url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(url + "users").json()
    data_to_export = {}
    for user in user_response:
        user_id = user["id"]
        todo_response = requests.get(url + f"todos?userid={user_id}").json()

    data_to_export[user_id] = [
            {
                "username": user.get("username"),
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                }
            for todo in todo_response
            ]
    return data_to_export


if __name__ == "__main__":
    data_to_export = fetch_all_user()
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data_to_export, jsonfile)
