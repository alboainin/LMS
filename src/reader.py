data = []

def garther():

    workbook = openpyxl.load_workbook('data.xlsx')
    worksheet = workbook.get_sheet_by_name('Sheet1')
    for cell in worksheet['E']:
        str(data)
        data.append(cell.value)
        
