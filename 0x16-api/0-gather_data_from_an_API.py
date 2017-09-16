#!/usr/bin/python3
"""
    A python script returns information about an employee's
    TODO list from a REST API
"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        user = argv[1]
        api_url = 'https://jsonplaceholder.typicode.com/'
        req_user = requests.get('{}users/{}'.format(api_url, user))
        name = req_user.json().get("name")
        if name is not None:
            json_req = requests.get(
                '{}todos?userId={}'.format(
                    api_url, user)).json()
            all_task = len(json_req)
            completed_task = []
            for task in json_req:
                if task.get("completed") is True:
                    completed_task.append(task)
            completed_count = len(completed_task)
            print("Employee {} is done with tasks({}/{}):"
                  .format(name, completed_count, all_task))
            for title in completed_task:
                print('\t {}'.format(title.get('title')))
