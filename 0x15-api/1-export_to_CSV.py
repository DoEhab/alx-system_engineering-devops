#!/usr/bin/python3
"""Print the completed tasks"""
import csv
import requests
import sys


if __name__ == "__main__":
    """pass user id and print the user tasks"""
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    file_name = "{}.csv".format(employee_id)

    try:
        user_data = requests.get(url + "users/{}".format(employee_id)).json()
        user_name = user_data.get("username")
        post_data = requests.get(url + "todos",
                                 params={"userId": employee_id}).json()
        with open(file_name, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_ALL)

            for data in post_data:
                writer.writerow(
                    [employee_id, user_name, data.get("completed"),
                     data.get("title")]
                )
    except requests.exceptions.RequestException as e:
        print(e)
