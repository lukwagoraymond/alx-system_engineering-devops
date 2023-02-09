#!/usr/bin/python3
"""
Uses REST API to get information about a given
employee's TO-DO list progress based on a given
employee ID and exports to json format
"""
import json
import requests
from sys import argv

if __name__ == '__main__':
    emp_id = argv[1]
    emp_url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    r_employ = requests.get(emp_url)
    employeeName = r_employ.json().get('username')

    todos_url = emp_url + "/todos"
    r_todos = requests.get(todos_url).json()
    total_num_task = r_todos
    completedTasks = []

    for task in r_todos:
        report_dict = dict()
        report_dict['username'] = str(employeeName)
        report_dict['completed'] = str(task.get("completed"))
        report_dict['task'] = str(task.get("title"))
        completedTasks.append(report_dict)
    report = dict()
    report[emp_id] = completedTasks

    with open("{}.json".format(emp_id), "w") as f:
        json.dump(report, f)
