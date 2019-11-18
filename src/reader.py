import openpyxl

reader_data = []
clean_data=[]

#short codes
bio = "BIO"
chemisry="CHE"
classic = "CLA"
activityBook = "ACT"

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

garther()
