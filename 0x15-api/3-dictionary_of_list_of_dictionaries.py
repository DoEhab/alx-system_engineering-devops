#!/usr/bin/python3
""" Print the completed tasks"""
import requests
import json


if __name__ == "__main__":
    """pass user id and print the user tasks"""
    url = "https://jsonplaceholder.typicode.com/"
    file_name = "todo_all_employees.json"
    my_data = []
    data = {}
    try:
        user_data = requests.get(url + "users").json()
        for user in user_data:
            uid = user.get("id")
            name = user.get("name")
            post_data = requests.get(url + "todos", params={"userId": uid}).json()
            for post in post_data:
                my_data.append({"username": name, "task": post.get("title"), "completed": post.get("completed")})
            data[uid] = my_data
        with open(file_name, mode="w", encoding="utf-8") as file:
            json.dump(data, file)
    except requests.exceptions.RequestException as e:
        print(e)
