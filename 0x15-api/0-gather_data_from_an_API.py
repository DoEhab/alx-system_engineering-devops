#!/usr/bin/python3
"""Print the completed tasks"""
import requests
import sys


if __name__ == "__main__":
    """pass user id and print the user tasks"""
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    try:
        user_data = requests.get(url + "users/{}".format(employee_id)).json()
        post_data = requests.get(url + "todos",
                                 params={"userId": employee_id}).json()
        completed_tasks = []
        for data in post_data:
            if data.get("completed") is True:
                completed_tasks.append(data.get("title"))
        print(
            "Employee "
            + user_data.get("name")
            + "is done with ({}/{}):"
            .format(len(completed_tasks), len(post_data))
        )
        for task in completed_tasks:
            print("     " + str(task))
    except requests.exceptions.RequestException as e:
        print(e)
