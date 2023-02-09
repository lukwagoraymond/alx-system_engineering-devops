#!/usr/bin/python3
"""
Uses REST API to get information about a given
employee's TO-DO list progress based on a given
employee ID
"""
import requests
from sys import argv

if __name__ == '__main__':
    emp_id = argv[1]
    emp_url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    r_employ = requests.get(emp_url)
    employeeName = r_employ.json().get('name')

    todos_url = emp_url + "/todos"
    r_todos = requests.get(todos_url).json()
    total_num_task = r_todos
    completedTasks = []

    for task in r_todos:
        if task.get('completed'):
            completedTasks.append(task)
    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, len(completedTasks), len(total_num_task)))

    for task in completedTasks:
        print("\t {}".format(task.get('title')))
