#!/usr/bin/python3
"""
Uses REST API to get information about a given
employee's TO-DO list progress based on a given
employee ID and exports to json format
"""
import json
import requests

if __name__ == '__main__':
    base_url = "https://jsonplaceholder.typicode.com/users"
    r_employs = requests.get(base_url).json()
    report = dict()

    for employ in r_employs:
        emp_id = employ.get("id")
        employeeName = employ.get('username')
        emp_url = "https://jsonplaceholder.typicode.com/users/{}"\
            .format(emp_id)
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
        report[emp_id] = completedTasks

    with open("todo_all_employees.json", "w") as f:
        json.dump(report, f)
