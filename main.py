
import sys
import json
import os
from utils import *
sys.path.append("./py_scripts")
from json_tasks import json_tasks
from shell_env import shell_task_1, shell_task_2

def main_loop():
    os.system("clear")
    print("DATA SCIENCE LABS\n\nQ - exit Data Science Labs\nS - view your scores\nEnter - Start Labs")
    # fork main path to score process or lab process
    command_1 = input("")
    if command_1.lower() == 's':
        # print formatted scores from ./lab_data/user_scores.json
        read_all_scores()
    elif command_1 == "":
        os.system("clear")
        topics = ["Shell Scripting", "Linux"]
        print("LABS\n")
        print("Which topic would you like to view?")
        for i in topics:
            print(f"\n  {i}")

        user_input = input("\nTopic: ")
        
        if user_input.lower() == "shell scripting":
            shell_task_1()
            shell_task_2()
        elif user_input.lower() == "linux":
            with open('./lab_data/linux_data.json', 'r', encoding="latin-1") as labs:
                data = json.load(labs)
                json_tasks(data['labs'], "Linux")
    elif command_1.lower() == "q":
            os.system("clear")
            return
    return main_loop()

main_loop()