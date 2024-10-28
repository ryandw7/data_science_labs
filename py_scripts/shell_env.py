import subprocess
from pathlib import Path
import sys
sys.path.append("../")
from utils import *
general_guide = "hit ctr+z to exit py, type fg once completed to check your work"
         
task1_instructions = "Create a file called sport.bash\n  1. Make it executable\n  2. Accept two parameters: NAME and SPORT\n  3. Display any sentence to the console using those inputs"

task2_instructions = "Write a script called counter.bash\n   A. It should count from 1 to the number entered by the user\n   B. Through the loop, display the current count value\n   C. Once the loop terminates, display “Loop Finished"

def handle_incorrect(task):
    print("q - back to menu\nn - move on\nany other key - check work again")
    nav_input = input("")
    if nav_input == "n":
        return True
    else:
        return task()

def instruct(task_instructions):
    print(f"{task_instructions}\n\n{general_guide}")
    block = input("")

def shell_task_1():

    instruct(task1_instructions)

    done = False
    correct_count = 0

    #while done == False:

    bash_file = Path("./sport.bash")
    if bash_file.is_file():
        subprocess.run(["chmod", "+rwx", "sport.bash"])
        correct_count += 1
        cat_bash = str(subprocess.run(["cat","./sport.bash"], stdout=subprocess.PIPE).stdout)
        
        if "#!/bin/bash" in cat_bash:
            correct_count += 1

            if "NAME=$" in cat_bash:
                correct_count += 1
            else:
                print("Missing NAME input")
            if "SPORT=$" in cat_bash:
                correct_count += 1
            else:
                print("Missing SPORT input")

            result = subprocess.run(["./sport.bash", "foo", "bar"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            if "foo" in result.stdout:
                correct_count += 1
            else:
                print("The name input isn't working correctly, try again")
            if "bar" in result.stdout:
                correct_count += 1
            else:
                print("The sport input isn't working correctly")

            if correct_count == 5:
                print("nice job!")
                done = True
                return True
        else:
            print("Try inserting #!/bin/bash at the top of your bash file.")
    else:
        print('sport.bash could not be found.\n try using "vi sport.bash"')
    if correct_count == 6:
        mark_completed("Shell Scripting", "Favorite Sport")
        print("nice job!")
            
        correct_block = input("\nPress any key to continue\n")
        done = True

    else:

        if handle_incorrect(shell_task_1) == True:
            
            done = True
        


def shell_task_2():

    instruct(task2_instructions)
    
    correct = 0
    done = False

    while done == False:

        bash_file = Path('./counter.bash')

        if bash_file.is_file():
            correct += 1
            cat_bash = str(subprocess.run(["cat", "counter.bash"], stdout=subprocess.PIPE).stdout)
            if "#!/bin/bash" in cat_bash:

                correct += 1

                subprocess.run(["chmod","+rwx","counter.bash"])
                result = subprocess.run(["./counter.bash", "5"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout
                
                if "COUNT=1" in cat_bash:
                    correct += 1
                else:
                    print("Count variable missing. Try inserting 'COUNT=1' to counter.bash")

                if "END=$1" in cat_bash:
                    correct += 1
                else:
                    print("End paramater missing. Try inserting 'END=$1' to counter.bash")

                conditions = ["1" in result, "2" in result, "3" in result, "4" in result, "5" in result]
                if all(conditions):
                    correct += 1
                else:
                    print('The value of COUNT is not being displayed. Try inserting >> echo "COUNT " = $COUNT << into counter.bash.')

                if "loop finished" in result.lower():
                    correct += 1
                else:
                    print(" stdout 'Loop Finished' was not found. Try inserting >> echo 'Loop Finished' << into counter.bash.")
                    print(result)

            else:
                print("Try inserting #!/bin.bash to the top of counter.bash")

        else:
            print("Try using 'vi counter.bash' to create a file")

        if correct == 6:
            print("Nice job!")
            mark_completed("Shell Scripting", "Favorite Sport")
            correct_block = input("\nPress any key to continue\n")
            done = True
        else:
            if handle_incorrect() == True:
                done = True
