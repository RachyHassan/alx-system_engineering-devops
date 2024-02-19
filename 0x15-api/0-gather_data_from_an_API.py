#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
Requirements:
    The script must accept an integer as a parameter, which is the employee IDi
    The script must display on the standard output the employee
    TODO list progress in this exact format:
    First line: Employee EMPLOYEE_NAME is done with tasks
    (NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
        EMPLOYEE_NAME: name of the employee
        NUMBER_OF_DONE_TASKS: number of completed tasks
        TOTAL_NUMBER_OF_TASKS: total number of tasks,
        which is the sum of completed and non-completed tasks
        Second and N next lines display the title of completed tasks:
        TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
"""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    employee_id = sys.argv[1]
    user_response = (requests.get(url + "users/{}".format(employee_id))).json()

    params = {"userId": employee_id}
    todos = (requests.get(url + "todos", params=params)).json()

    completed_tasks = [t.get("title") for t in todos if t.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format
          (user_response.get("name"), len(completed_tasks), len(todos)))
    [print("\t {}".format(complete)) for complete in completed_tasks]
