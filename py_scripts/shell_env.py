import subprocess
from pathlib import Path
def shell_task_1():
    print('Create a file called sport.bash\n 1. Make it executable\n 2. Accept two parameters: NAME and SPORT\n 3. Display any sentence to the console using those inputs')
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
            print("nice job!")
    else:
        print('sport.bash could not be found.\n try using "vi sport.bash"')

