\import os
import sys


location = r'\\HOST\programs'
main_file = ".lms"
path =os.path.join(location,main_file)

folder = "data"
path_sub =os.path.join(path,folder)

account = "account"
account_path = os.path.join(path,account)

admin_account = "admin"
student_account = "student"

def cls():
    os.system("Cls" if os.name =="nt" else "clear")

def file_init():
   
    try:
        if os.path.isdir(path):
            cls()
            print("Main Directory Exists!")

        else:
            os.chdir(location)
            os.mkdir(main_file)
            os.system(f'attrib +h {path}')
            cls()
            print("Directory Created!")

    except:
        print("[ERROR] TRY AGAIN")
    
def sub_folder():   
    if os.path.isdir(path_sub):
        print(f'{folder} Directory Exists!')

    else:
        os.chdir(path)
        os.mkdir(folder)
        print(f'{folder} Directory Created!')


def account_folder():
    if os.path.isdir(account_path):
        print(f'{account} Directory Exists!')

    else:
        os.chdir(path)
        os.mkdir(account)
        print(f'{account} Directory Created!')


def account_files():
    os.chdir(account_path)

    if os.path.exists(admin_account):
        pass
    
    else:
        with open(f'{admin_account}.json','a+') as data:
            print("file created")

    if os.path.exists(student_account):
        pass
    
    else:
        with open(f'{student_account}.json','a+') as data:
            pass
            
