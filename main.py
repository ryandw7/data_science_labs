import sys
import json
sys.path.append("./py_scripts")
from json_tasks import json_tasks
from shell_env import shell_task_1
topics = ["Shell Scripting", "Linux"]
print("Which topic would you like to view?")
for i in topics:
    print(f"\n  {i}")

user_input = input("\nTopic: ")

if user_input == "Shell Scripting":
    shell_task_1()
elif user_input == "Linux":
    with open('./lab_data/linux_data.json', 'r', encoding="latin-1") as labs:
        data = json.load(labs)
        json_tasks(data['labs'])
