import subprocess
from pathlib import Path
import time
def shell_task_1():
    done = False
    while done == False:
        print('Create a file called sport.bash\n  1. Make it executable\n  2. Accept two parameters: NAME and SPORT\n  3. Display any sentence to the console using those inputs')
        print('hit ctr+z to exit py, type fg once completed to check your work')
        user_input = input('')
        correct_count = 0
        bash_file = Path("./sport.bash")
        if bash_file.is_file():

            correct_count += 1

            subprocess.run(["chmod","+x","sport.bash"])

            cat_bash = subprocess.run(["cat","./sport.bash"], stdout=subprocess.PIPE)
            cat_str = str(cat_bash.stdout)

            if "NAME=$" in cat_str:
                correct_count += 1
            else:
                print("Missing NAME input")
            if "SPORT=$" in cat_str:
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
                done = True
                return True
                print("nice job!")
            else:
                print('sport.bash could not be found.\n try using "vi sport.bash"')
                time.sleep(3)
                user_input = input("Hit enter to retry")

def shell_task_2():
    correct = 0
    print("Write a script called counter.bash\n   A. It should count from 1 to the number entered by the user\n   B. Through the loop, display the current count value\n   C. Once the loop terminates, display “Loop Finished”")
    print("\nhit ctr+z to exit py, type fg once completed to check your work")
    block = input("")
    bash_file = Path('./counter.bash')
    if bash_file.is_file():
        correct += 1
    else:
        print("Can't find file: counter.bash")
    subprocess.run(["chmod","+rwx","counter.bash"])
    result = subprocess.run(["./counter.bash", "5"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout
    cat_bash = str(subprocess.run(["cat", "counter.bash"], stdout=subprocess.PIPE).stdout)

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
    if correct == 5:
        print("Nice Job!")
        return True
    else:
        print("sorry :/")
        return False

