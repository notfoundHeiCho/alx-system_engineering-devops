## API

## Tasks 📃:

# 0.Gather data from an API:
    💠 Python script that returns information on the to-do list progress of a given employee ID.
    💠 Usage: ```python3 0-gather_data_from_an_API.py <employeeID>```.
    💠 Output: ```Employee <employee name> is done with tasks (<# completed tasks>/<total # tasks>):```

# 1. Export to CSV:
    💠 Python script exports to-do list information of a given employee ID to CSV format.
    💠 Usage: ```python3 1-export_to_CSV.py <employee ID>```
    💠 File name: ```<user id>.csv```.
    💠 Format: ```"<user id>","<username>","<task completed status>","<task title>"```.

# 2-Export to JSON:
    💠 Python script that exports to-do list information of a given employee ID to JSON format.
    💠 Usage: ```python3 2-export_to_JSON.py <employee ID>```
    💠 File name: ```<user id>.json```
    💠 Format: ```{"<user id>": [ {"task": "<task title>", "completed": <task completed status>, "username": "<username>}, ... ]}```

# 3- Dictionary of list of dictionaries:
    💠 Python script that exports to-do list information for all employees to JSON format.
    💠 Usage: ```python3 3-dictionary_of_list_of_dictionaries.py```
    💠 File name: ```todo_all_employee.json```
    💠 Format: ```{ "<user id>": [ {"username": "<username>", "task": "<task title>", "completed": <task completed status>}, {"username": "<username>", "task": "<task title>", "completed": <task completed status>}, ... ], "<user id>": [{"username": "<username>", "task": "<task title>", "completed": <task completed status>}, {"username": "<username>", "task": "<task title>", "completed": <task completed status>}, ... ]}```
