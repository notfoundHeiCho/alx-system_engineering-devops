#!/usr/bin/python3
"""A script that gathers data from an API
"""
import requests
from sys import argv


def main():
    """main function"""
    BASE_URL = 'https://jsonplaceholder.typicode.com/'
    id_user = argv[1]
    user = requests.get(BASE_URL + 'users/{}'.format(id_user)).json()
    todos = requests.get(BASE_URL + 'todos', params={'userId': id_user}).json()
    length = 0
    completed_tasks = []
    for task in todo:
        if task.get('completed') is True:
            completed_tasks.append(task.get('title'))
            length += 1
    name = user.get('name')
    print(f"Employee {name} is done with tasks({length}/{len(todo)}):")
    [task for task in completed_tasks if print(f"\t {task}")]


if __name__ == '__main__':
    main()
