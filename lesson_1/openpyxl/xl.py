from openpyxl import Workbook  # 從openpyxl套件中 載入workbook
wb = Workbook()   # Workbook is an object not function 

# grab the active worksheet
ws = wb.active

# Data can be assigned directly to cells
ws['A1'] = 42
ws['B1'] = 'Nicky'
# Rows can also be appended
ws.append([1, 2, 3])

# Python types will automatically be converted
import datetime
ws['A2'] = datetime.datetime.now()

# Save the file
wb.save("sample.xlsx")   # 檔名可以自設