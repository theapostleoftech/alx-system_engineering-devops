#!/usr/bin/python3
"""
A script to export a uswer data to json
"""

import json
import requests
import sys


def get_data_from_api(employee_id):
    """
    This function retrieves data from api
    and exports it to CSV
    """
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = employee_url + "/todos"
    employee_response = requests.get(employee_url)
    todos_response = requests.get(todo_url)
    employee = employee_response.json()
    todos = todos_response.json()

    employee_username = employee.get('username')
    todo_data = []

    for task in todos:
        todo = {}
        todo["username"] = str(employee_username)
        todo["completed"] = task.get("completed")
        todo["task"] = str(task.get("title"))
        todo_data.append(todo)

    response = {}
    response[employee_id] = todo_data
    return response


def export_to_json(todo_data, employee_id):
    filename = f"{employee_id}.json"
    with open(filename, "w") as json_file:
        json.dump(todo_data, json_file, indent=2)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        todo_data = get_data_from_api(employee_id)
        export_to_json(todo_data, employee_id)
    except ValueError:
        print("Invalid employee ID. Please provide a valid integer.")
