import json
import sys
sys.path.append('../')
from utils import *

def json_tasks(lab, topic):
    #Functions to handle each task type
    #Returns true if correct, false if incorrect
    
    def handle_single_answer_task(task):
        user_input = input("")
        correct_answer = task['answer']
        if user_input == correct_answer:
            return True
        else:
            return False
        
    def handle_multi_choice_task(task):
        for choice in task['answers']:
            print('    ' + choice)
        user_answer = input("\nYour answer: ")
        answer = task['answer']
        if user_answer == answer:
            return True
        else:
            return False

    def handle_table_task(task):
        total_correct = 0
        total_incorrect = 0
        print(f"{task['format']}\n")
        for i, item in enumerate(task['values']):
            user_input = input(f"{item} ")
            correct_answer = str(task['answers'][i]).strip()
            if user_input.strip() == correct_answer:
                total_correct += 1
            else:
                print(correct_answer, user_input, type(correct_answer), type(user_input))
                total_incorrect += 1
        if total_correct == 3:
            print("3 of 3 correct.")
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

    def handle_multi_answer_task(task):
                user_answer = input("Your answer: ")
                correct_answers = task['answers']
                if user_answer in correct_answers:
                    return True
                else:
                    return False

    # Function to be executed on each task
    # is_correct takes task handlers as argument
    def handle_task(task, is_correct):
        if is_correct:
            print('\ngood job!\n')
            return True
        else:
            print('\nIncorrect.\n')
            answer_format = ''
            if task['type'] == 'table' or task['type'] == 'multi-answer':
                answer_format = 'answers'
            elif task['type'] == 'single-answer' or task['type'] == 'multi-choice':
                answer_format = 'answer'
                
            prompt_answer = input(f"Would you like to see the {answer_format}?\n Type 'y' for yes, or enter for no. ")
            if prompt_answer == 'y':
                if answer_format == 'answer':
                    print(f"\n{task['answer']}")
                elif answer_format == 'answers':
                    for i in task['answers']:
                        print(f"\n{i}")
                  
                continue_tasks = input("")
            return False    


    def show_labs():
        print("")
        for item in lab:
            print(f"   {item['name']}\n")
        
    show_labs()

    lab_input = input("which would you like to review?\n")
    selected_lab = ''
    for item in lab:
        if item['name'] == lab_input:
            selected_lab = item
    def res_lab_input():
        if selected_lab:
            print("\nLet's get started!\n")
        else:
            print("\nSorry, that's not an option!\n")

    res_lab_input()

    # Stores tasks in task variable and runs handle task through each task
    
    correct = 0
    incorrect = 0
    subtopic = selected_lab['name']
    for task in selected_lab['tasks']:

        print(f"{task['prompt']}\n")
        if task['type'] == 'single-answer':
            if handle_task(task, handle_single_answer_task(task)):
                correct += 1
            else:
                incorrect += 1
        elif task['type'] == 'multi-choice':
            if handle_task(task, handle_multi_choice_task(task)):
                correct += 1
            else:
                incorrect += 1
        elif task['type'] == 'multi-answer':
            if handle_task(task, handle_multi_answer_task(task)):
                correct += 1
            else:
                incorrect += 1
        elif task['type'] == 'table':
            if handle_task(task, handle_table_task(task)):
                correct += 1
            else:
                incorrect += 1
        print("============================================")
        # after loop, prints results
        total_tasks = len(selected_lab["tasks"])
        total_correct = correct
        total_incorrect = incorrect
        percent_correct = round(total_correct / total_tasks * 100)
        
        write_score(topic, subtopic, total_correct)
    print(f"""
        Total Tasks: {total_tasks}\n
        Total Correct: {total_correct}\n
        Total Incorrect: {total_incorrect}\n
        Percent Correct: {percent_correct}\n
        """)

