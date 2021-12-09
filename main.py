import gspread
import re

gc = gspread.service_account('secrets.json')

spreadsheet = gc.open('weather_private')

# get worksheet by index
worksheet1 = spreadsheet.get_worksheet(0)

# get worksheet by name 
worksheet1 = spreadsheet.worksheet('2013')
# print(worksheet1)

# data = worksheet1.get_all_records()
# print(data[10])  # gets only the 10th row

data = worksheet1.get_values('A5:F7') # Gets a list of lists
# print(data)

# get a column
column = worksheet1.get_values('F2:F25')
# print(column)

#better way to get column values
col = worksheet1.col_values(2) # gets a list
# print(col)

# get a cell
cell = worksheet1.get_values("D5")
# print(cell)

# better way to get a cell
cell = worksheet1.acell("D5").value
# print(cell)

# search for which cell contains a value
cell3 = worksheet1.find('-10')
# print(cell3)  # gets an object 
# print(cell3.row, cell3.col)  # gets the row and column

# search for many cells
# cells = worksheet1.findall("-9")
# cells3 = [(cell.row,cell3.col) for cell in cells]
# print(cells3)

# search for cells containing a Value
req = re.compile(r'99')
cells = worksheet1.findall(req)
# print(cells)

# update a cell's Value
# worksheet1.update('E5', -29)

#update cell value based on row-col
# worksheet1.update_cell(5,5,-39)

#to change values of a col and add a new col
existing = worksheet1.get_values('E2:E25')
new_col = [[round((float(i[0])*9/5+32), 1)] for i in existing]
print(new_col)
worksheet1.update('G1:G2', [['Fahreneit']] + new_col)