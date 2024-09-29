import sys
sys.path.append("./py_scripts")
from linux_labs import linux_labs
from shell_env import shell_task_1
topics = ["Shell Scripting", "Linux"]
print("Which topic would you like to view?\n")
for i in topics:
    print(i)

user_input = input("\nTopic: ")

if user_input == "Shell Scripting":
    shell_task_1()
elif user_input == "Linux":
    linux_labs()
