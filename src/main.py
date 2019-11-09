import getpass
import json
import os

def cls():
    os.system("Cls" if os.name =="nt" else "clear")
    
def ManageBook():
    cls()
    ''' 
    with open("book_data.json","r") as read_data:
        data = json.load(read_data)

        for enum in range(data[]):
        print("")
        '''
def addBook():
    print(f'{"*"*10}EDITING COLLECTION{"*"*10}')
    book_genre = str(input("genre: ")) 
    book_name = str(input("Enter book name: "))
    book_author = str(input("Enter book author: "))
    book_description = str(input("description: "))
    
    with open("book_data.json","r+") as data_pure:
        data = {}
        data[book_genre] = []

        data["genre"][book_genre].append({"name":book_name,"author":book_author,"description":book_description,"genre":book_genre})
 
        data_pure.seek(0)
        json.dump(data,data_pure)
        print("Book Added Succesfully!")
        cls()

def login():

    print(f'{"*"*10} STUDENT LOGIN {"*"*10}')

    student_loginUsername = str(input("username: "))
    student_loginPassword = getpass.getpass(prompt="password: ")
        
    with open("accounts.json","r+") as data:
        user_account = json.load(data)

        if student_loginUsername not in user_account.keys():
            print("An Account Of that username doesn't exist")

        elif student_loginUsername in user_account.keys():
                
            if user_account[student_loginUsername][0] != student_loginPassword:
                print("Your password is incorrect\nPlease try again")
                
            elif user_account[student_loginUsername][0] == student_loginPassword:
                print("Logged in Successfully!")
                    
                cls()
                print("Login Success As Student")
            else:
                cls()
                print("PLEASE CREATE AN ACCOUNT!")

def student_signIn():
    
    username = input("username: ")
    password = getpass.getpass(prompt= "password: ")

    with open("accounts.json","r+") as student_account:
        user_account = json.load(student_account)

        if username in user_account.keys():
            print("An account of this Username already exists.\nPlease enter the login panel.")
      
        else:
            user_account[username] = [password, "Student"]
            student_account.seek(0)
            json.dump(user_account,student_account)
            print("Account Created Successfully!")   

def student():
   
    
    print("1) Login")
    print("2) Create Account")
    
    try:
        user_input = int(input(">  "))
    
    except:
        warning = "> [WARNING] please choose on of the options" 
        print(warning.upper())
    
    if user_input == 1:
        login()

    elif user_input == 2:
        student_signIn()

def admin():
    
    
    count = 1
    while count !=4:
        cls()
        exp = 1
        print(f'{"*"*10} ADMIN LOGIN {"*"*10}')
    
        admin_loginUsername = input("username: ")
        admin_loginPassword = getpass.getpass(prompt = "password: ")
    
        with open('accounts.json') as f:
            data_file = json.load(f)
    
        for data in data_file['admin_account']:
          
            if admin_loginUsername == data["username"]:
                if admin_loginPassword == data["password"]:
                    cls()
                    break
                    
        if admin_loginUsername == data["username"] and admin_loginPassword == data["password"]:
            break

        count += 1

        if count == 4:
            print("3 Incorrect Tries")
            break

    while exp != 3:
        print(f'{"*"*10}ADMIN PAGE{"*"*10}\n')
        print("1) Add Book")
        print("2) Browse Library")
        print("3) Exit\n")
        try:
            user_input = int(input("> "))
         
        except:
            warning = "> [WARNING] please choose on of the options" 
            print(warning.upper())
        
        if user_input == 1:
            addBook()

        elif user_input == 2:
            manageBook()
        
        elif user_input == 3:
            break

def guest():
    pass

def menu():
    cls()
    user_menu = 1

    while user_menu !=4:
        print(f'{"*"*10} MENU {"*"*10}\n')
        print("1) Admin")
        print("2) Student")
        print("3) Guest")
        print("4) Exit\n")
        
        try:   
            user_menu = int(input("> "))
        
        except:
            warning = "> [WARNING] please choose on of the options" 
            print(warning.upper())

        if user_menu == 1:
            admin()
            input("")
            cls()

        elif user_menu == 2:
            student()
            input("")
            cls()
        
        elif user_menu == 3:
            guest()
            input("")
            cls()

        elif user_menu == 4:
            break
        
        else:
            cls()

menu()
