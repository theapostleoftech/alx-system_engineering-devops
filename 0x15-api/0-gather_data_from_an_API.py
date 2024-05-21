#!/usr/bin/python3
""" A script to return TODO information
about an employee
"""

import requests
import sys


def get_data_from_api(employee_id):
    employee_url = f"https://jsonplaceholder.typicode.com/users/userId={employee_id}"
    todo_url = employee_url + "/todos"
    employee_response = requests.get(employee_url)
    todos_response = requests.get(todo_url)
    employee = employee_response.json()
    todos = todos_response.json()

    employee_name = todos[0]['userId'] if todos else 'Unknown'
    employee_name = employee.get('name')
    total_tasks = len(todos)
    completed_tasks = [task['title'] for task in todos if task['completed']]
    num_of_compelted_tasks = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, num_of_compelted_tasks, total_tasks))
    for task in completed_tasks:
        print(f"\t {task}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_data_from_api(employee_id)
    except ValueError:
        print("Invalid employee ID. Please provide a valid integer.")
    pass
