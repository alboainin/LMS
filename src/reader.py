import openpyxl
import os

reader_data= []
clean_data=[]
catagory_list=[]

def dump():
    pass

def garther():

    global reader_data
    workbook = openpyxl.load_workbook('data.xlsx')
    worksheet = workbook.get_sheet_by_name('Sheet1')
    
    for cell in worksheet['E']:
        reader_data = cell.value
    
    for col in worksheet['B']:
        if "BIO" in str(col.value):
            print("yes")
        else:
            print("eror")

def sender():

    workbook = openpyxl.load_workbook('data.xlsx')
    worksheet = workbook.get_sheet_by_name('pure-data')
    
    pwd = os.getcwd()
    dir = "data"
    path = os.path.join(pwd,dir)   
        
    if os.path.isdir(path):
        os.chdir(dir)
        
    else:
        os.mkdir(path)

    for cell in worksheet['E']:
        
        data_lower = cell.value
        data = data_lower.lower()
        
        catagory_list.append(data)
        catagory_list.sort()
               
        for filename in catagory_list:
            os.chdir(path)
        
            with open(f'{filename}.json','a+') as file:
                data = file.read()
        
