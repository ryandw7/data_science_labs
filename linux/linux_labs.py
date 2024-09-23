import json

with open('linux_data.json') as file:
    data = json.load(file)
    labs = data['labs']
    def show_labs():
        for item in labs:
            print(f"   {item['name']}\n")
    print("Here are the labs you can review:\n")
    show_labs()

    lab_input = input("\nwhich would you like to review?\n\n")
    lab = ''

    for item in labs:
        if item['name'] == lab_input:
            lab = item
    def res_lab_input():
        if lab:
            print("Let's get started!\n")
        else:
            print("Sorry, that's not an option!")

    res_lab_input()

    def handle_table_task(task):
        total_correct = 0
        total_incorrect = 0
        print(task['prompt'])
        for i, item in enumerate(task['values']):
            print(task["format"])
            user_input = input(f"{item} ")
            correct_answer = str(task['answers'][i]).strip()
            print(task['answers'][i])
            if user_input.strip() == correct_answer:
                total_correct += 1
                print('correct')
            else:
                print(correct_answer, user_input, type(correct_answer), type(user_input))
                total_incorrect += 1
       
        if total_correct == 3:
            print("Nice Job! 3 of 3 correct.")
            return True
        elif total_correct == 2:
            print("2 of 3 correct.")
            return False
        elif total_correct == 1:
            print("1 of 3 correct.")
            return False
        else:
            print("0 of 3 correct.")
            return False
    


    #Begin tasks after successfully determing lab

    tasks = lab['tasks']
    correct = 0
    incorrect = 0
    for task in tasks:
        if task['type'] == 'single-answer':
                print(f"{task['id']}. {task['prompt']}")
                user_answer = input("Your answer: ")
                answer = task['answer']
                if user_answer == answer:
                    print('Nice Job!\n')
                    correct += 1
                else:
                    print(f"Wrong answer :/\n The correct answer is: \n {answer}\n")
                    incorrect += 1

                print('=====================================================\n')

        if task['type'] == 'multi-answer':
            print(f"{task['id']}. {task['prompt']}")
            user_answer = input("Your answer: ")
            correct_answers = task['answers']
            if user_answer in correct_answers:
                print('Nice Job!\n')
                correct += 1
            else:
                print(f"Wrong answer :/\n The correct answer is: \n {answer}\n")
                incorrect += 1
                print('=====================================================\n')

        if task['type'] == 'multi-choice':
            print(f"{task['id']}. {task['prompt']}")
            for choice in task['answers']:
                print('    ' + choice)
            user_answer = input("\nYour answer: ")
            answer = task['answer']
            if user_answer == answer:
                print('Nice Job!\n')
                correct += 1
            else:
                print(f"Wrong answer :/\n The correct answer is: \n {answer}\n")
                incorrect += 1

            print('=====================================================\n')
        if task['type'] == 'table':
            if handle_table_task(task) == True:
                correct += 1
            else:
                incorrect += 1
            print('=====================================================\n')
    total_tasks = len(tasks)
    total_correct = correct
    total_incorrect = incorrect
    percent_correct = round(total_correct / total_tasks * 100, 2)

    print(f"""
    Total Tasks: {total_tasks}\n
    Total Correct: {total_correct}\n
    Total Incorrect: {total_incorrect}\n
    Percent Correct: {percent_correct}\n
    """)

