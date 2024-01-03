#!/usr/bin/python3
"""A Python script that, using a REST API, for a given employee ID, returns
information about his/her TODO list progress and
exports data in JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    employee_id = sys.argv[1]

    user_response = requests.get(url + "users/{}".format(employee_id))

    if user_response.status_code != 200:
        print("Error: User not found.")
        sys.exit(1)

    user = user_response.json()

    todos_response = requests.get(url + "todos",
                                  params={"userId": employee_id})
    todos = todos_response.json()

    # Prepare JSON data
    json_data = {employee_id: [{"task": todo["title"],
                                "completed": todo["completed"],
                                "username": user["username"]}
                 for todo in todos]}

    # Export data to JSON file
    json_file_name = "{}.json".format(employee_id)
    with open(json_file_name, 'w') as json_file:
        json.dump(json_data, json_file)

    print("Data exported to: {}".format(json_file_name))
