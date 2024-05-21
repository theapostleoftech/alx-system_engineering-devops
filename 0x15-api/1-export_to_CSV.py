#!/usr/bin/python3
"""
A python script to export data in the CSV format
"""

import csv
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
        todo["USER_ID"] = str(task.get("userId"))
        todo["USERNAME"] = str(employee_username)
        todo["TASK_COMPLETED_STATUS"] = str(task.get("completed"))
        todo["TASK_TITLE"] = str(task.get("title"))
        todo_data.append(todo)


def export_to_csv(todo_data, employee_id):
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.Dictwriter(csvfile)
        writer.writerow(
            [
                "USER_ID",
                "USERNAME",
                "TASK_COMPLETED_STATUS",
                "TASK_TITLE"
                ])
        writer.writerows(todo_data)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        todo_data = get_data_from_api(employee_id)
        export_to_csv(todo_data, employee_id)
    except ValueError:
        print("Invalid employee ID. Please provide a valid integer.")
