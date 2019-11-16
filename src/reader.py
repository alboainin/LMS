import openpyxl

def garther():
    workbook = openpyxl.load_workbook('data.xlsx')
    worksheet = wb.get_sheet_by_name('Sheet1')
    for cell in ws['E']:
        print(cell.value)
    
