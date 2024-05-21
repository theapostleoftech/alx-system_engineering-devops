#!/usr/bin/python3
"""
A script to export data in json format
"""

import json
import requests


def get_data_from_api():
    employee_url = f"https://jsonplaceholder.typicode.com/users/"
    employee_response = requests.get(employee_url)
    employees = employee_response.json()
    response = {}

    for employee in employees:
        employee_id = employee.get('id')
        todo_url = employee_url + "/{}/todos".format(employee_id)
        todos_response = requests.get(todo_url)
        todos = todos_response.json()

        employee_username = employee.get('username')

        todo_data = []

        for task in todos:
            todo = {}
            todo["username"] = str(employee_username)
            todo["completed"] = task.get("completed")
            todo["task"] = str(task.get("title"))
            todo_data.append(todo)

        response[employee_id] = todo_data

    return response


def export_to_json(todo_data):
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(todo_data, json_file, indent=2)


if __name__ == "__main__":
    todo_data = get_data_from_api()
    export_to_json(todo_data)
