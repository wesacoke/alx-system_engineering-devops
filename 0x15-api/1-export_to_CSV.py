#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to CSV format.
"""
import csv
import requests
import sys

if __name__ == "__main__":
    # Define the base URL for the JSON API
    url = "https://jsonplaceholder.typicode.com/"

    user_id = 2

    # Fetch user information from the API and
    # convert the response to a JSON object
    user = requests.get(url + "users/{}".format(user_id)).json()

    # Extract the username from the user data
    username = user.get("username")

    # Fetch the to-do list items associated with the
    # giVen user ID  and convert the response to a JSON object
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Use list comprehension to iterate over the to-d- list items
    # Write each item's details (user ID, username, cimetion status,
    # and title) as a row in the CSV file
    with open("{}.csv".format(user_id), "w", newline="")as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
            ) for t in todos]
