import sys
import json
import asyncio
sys.path.append("./py_scripts")
from json_tasks import json_tasks
from shell_env import shell_task_1, shell_task_2
from utils import read_score
print("Press any key to start labs, press S to view scores")
command_1 = input("")
if command_1 == 's':
    read_score()
else:
    topics = ["Shell Scripting", "Linux"]
    print("Which topic would you like to view?")
    for i in topics:
        print(f"\n  {i}")

    user_input = input("\nTopic: ")
    
    if user_input == "Shell Scripting":
        shell_task_1()
        shell_task_2()
    elif user_input == "Linux":
        with open('./lab_data/linux_data.json', 'r', encoding="latin-1") as labs:
            data = json.load(labs)
            json_tasks(data['labs'])
