import json

#{
# "id": 1,
# "type": "fill-table",
# "prompt": "Fill in the permission sets and write the 3 digit octal number that represents the permission sets in the format:",
# "format":"owner, group, other, octal-value",
# "values": ["group", "skel", "motd"],
# "answers": ["rw-, r--, r--, 644", "rwx, r-x, r-x, 755", "rwx, rwx, rwx, 777"]
#},
def handle_table_task(task):
    total_correct = 0
    total_incorrect = 0
    print(task['prompt'])
    for i, item in enumerate(task['values']):
        print(task["format"])
        user_input = input(f"{item}")
        if user_input == task['values'][i]:
            total_correct += 1
            print('correct')
        else:
            total_incorrect += 1 
    if total_correct == 4:
        print("Nice job! 4 of 4 correct!")
        return True
    elif total_correct == 3:
        print("Almost, 3 of 4 correct.")
        return False
    elif total_correct == 2:
        print("2 of 4 correct.")
        return False
    elif total_correct == 1:
        print("1 of 4 correct.")
        return False
    else:
        print("0 of 4 correct.")
        return False
    



with open('linux_data.json') as f:
    data = json.load(f)
    labs = data['labs']
    table_task = labs[2]['tasks'][0]

    handle_table_task(table_task)
