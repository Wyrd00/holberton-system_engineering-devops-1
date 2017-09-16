#!/usr/bin/python3
"""
    Export to json file all tasks owned by an employee
"""
import json
import requests

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    req_user = requests.get("{}users".format(api_url)).json()
    user_dict = {}
    for user in req_user:
        username = user.get("username")
        user_id = user.get("id")
        all_tasks = requests.get(
            "{}todos?userId={}".format(
                api_url, user_id)).json()
        task_list = []
        for task in all_tasks:
            task_dict = {}
            task_dict["task"] = task.get("title")
            task_dict["completed"] = task.get("completed")
            task_dict["username"] = username
            task_list.append(task_dict)
        user_dict[user_id] = task_list
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(user_dict, jsonfile)
