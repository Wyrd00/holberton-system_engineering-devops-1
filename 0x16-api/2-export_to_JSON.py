#!/usr/bin/python3
"""
    Export to json file all tasks owned by an employee
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        user = argv[1]
        api_url = "https://jsonplaceholder.typicode.com/"
        req_user = requests.get("{}users/{}".format(api_url, user))
        username = req_user.json().get("username")
        all_tasks = requests.get(
            "{}todos?userId={}".format(
                api_url, user)).json()
        task_list = []
        user_dict = {}
        for task in all_tasks:
            task_dict = {}
            task_dict["task"] = task.get("title")
            task_dict["completed"] = task.get("completed")
            task_dict["username"] = username
            task_list.append(task_dict)
        user_dict[user] = task_list
        with open("{}.json".format(user), "w") as jsonfile:
            json.dump(user_dict, jsonfile)
