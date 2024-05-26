#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.

"""
import requests
import sys

if __name__ == "__main__":
    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    employee_id = 1

    # Get the employee using the provided emoloyee ID
    params = {"userId": employee_id}
    todos = requests.get(url + "todos", params=params).json()

    # Filter completed tasks and count them
    completed = [t.get("title") for t in todos if t.get("completed")]

    # Print the employee's name and the number of completed tasks
    print("Employee {} is done with tasks ({}/{}):".format(
        employee_id, len(completed), len(todos)))

    # Print the completed tasks one by one with indentation
    for complete in completed:
        print("\t{}".format(complete))
