#!/usr/bin/python3
"""script to get todos"""

import requests
import sys

def main():
	"""main function"""
	base_url = "https://jsonplaceholder.typicode.com/"
	employee_id = sys.argv[1]
	employee_info = requests.get(f"{base_url}users/{employee_id}").json()
	employee_name = employee_info["name"]

	todo_data = requests.get(f"{base_url}todos").json()
	result_todos ={}

	for item in todo_data:
		user_id = item["userId"]
		if user_id not in result_todos:
			result_todos[user_id] = {
				"completed_count": 0,
				"task_count": 0,
				"tasks": []
			}
		result_todos[user_id]["task_count"] += 1
		if item["completed"]:
			result_todos[user_id]["completed_count"] += 1
		result_todos[user_id]["tasks"].append(item["title"])

	if int(employee_id) in result_todos:
		employee_tasks = result_todos[int(employee_id)]
		print(
			f"Employee {employee_name} is done with tasks "
			f"({employee_tasks['completed_count']}/{employee_tasks['task_count']}):")
		for task_title in employee_tasks["tasks"]:
			print(f"\t {task_title}")
if __name_- == '__main__':
	main()
