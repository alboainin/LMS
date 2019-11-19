import os
import sys


location = r'\\host\programs'
main_file = ".lms"
path =os.path.join(location,main_file)

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
    
    folder = "data"
    path_sub = path+'\\'+folder
    
    if os.path.isdir(path_sub):
        print(f'{folder} Directory Exists!')

    else:
        os.chdir(path)
        os.mkdir(folder)
        print(f'{folder} Directory Created!')