#this script is just used to clear json file due to the tests that happened 
#during testing some functions thats envolve writtign to the json file

import os
import sys

cwd = os.getcwd() + "\\"

os.chdir("data")

os.remove("student_account.json")

with open("student_account.json", "a+") as file:
    pass