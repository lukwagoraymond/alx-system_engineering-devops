#!/usr/bin/python3
"""
Uses REST API to get information about a given
employee's TO-DO list progress based on a given
employee ID and exports to csv format
"""
import csv
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
        report_dict['USER_ID'] = str(task.get("userId"))
        report_dict['USERNAME'] = str(employeeName)
        report_dict['TASK_COMPLETED_STATUS'] = str(task.get("completed"))
        report_dict['TASK_TITLE'] = str(task.get("title"))
        completedTasks.append(report_dict)
    header = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    with open("{}.csv".format(emp_id), "w") as f:
        f_csv = csv.DictWriter(f, fieldnames=header, quoting=csv.QUOTE_ALL)
        f_csv.writerows(completedTasks)
