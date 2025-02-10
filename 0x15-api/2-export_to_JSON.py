#!/usr/bin/python3
""" Print the completed tasks"""
import csv
import json
import sys

import requests

if __name__ == "__main__":
    """pass user id and print the user tasks"""
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    file_name = "{}.json".format(employee_id)
    my_data = []

    try:
        user_data = requests.get(url + "users/{}".format(employee_id)).json()
        user_name = user_data.get("name")
        post_data = requests.get(url + "todos", params={"userId": employee_id}).json()
        for post in post_data:
            my_data.append({"task": post.get("title"), "completed": post.get("completed"), "username": user_name})
        data = {
            employee_id: my_data
        }
        with open(file_name, mode="w", encoding="utf-8") as file:
            json.dump(data, file)
    except requests.exceptions.RequestException as e:
        print(e)
