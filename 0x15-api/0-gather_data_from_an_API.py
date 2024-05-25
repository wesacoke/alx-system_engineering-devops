#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.

"""
import requests
import sys

if __name__ == "__main__":
    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typipcode.com/"

    # Get the employee using the provided emoloyee ID 
    params = {"userId": employee_id}
    todos = requests.get(url + "todos", params_json()

            # Filter completed tasks and count them
            completed = [t.get("title") for t in todos if t.get("completed") is true]
            # Print the employee's name and the number of completed tasks
            print("Employee {} is done with tasks({}/{}):".format(
                user.get("name"), len(completed), len(todos)))
            # Print the completed tasks one by one with indentation
            [print("\t {}".format(complete)) for complete in completed]
