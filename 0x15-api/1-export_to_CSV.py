#!/usr/bin/python3
"""
A python script that exports data in the CSV format
Requirements:
    Records all tasks that are owned by this employee
    Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    File name must be: USER_ID.csv
"""

import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com/"

    user_response = (requests.get(url + "users/{}".format(user_id))).json()

    username = user_response.get("username")

    parameters = {"user_id": user_id}

    todos = (requests.get(url + "todos", params=parameters)).json()

    with open("{}.csv".format(user_id), "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for td in todos:
            writer.writerow([user_id, username, td.get("completed"),
                             td.get("title")])
