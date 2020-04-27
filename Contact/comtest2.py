import win32com.client

excel = win32com.client.Dispatch("Excel.Application")

wb = excel.Workbooks.Open('D:\\Python\\prj\\learnpython\\file\\exceltest.xlsx')
ws = wb.ActiveSheet
print(ws.Cells(1, 1).Value)

ws.Cells(1, 2).Value = "배영규"
ws.Range("C1").Value = "좋아!"
ws.Range("C1").Interior.ColorIndex = 10

ws.Range("A2:C2").Interior.ColorIndex = 27

excel.Quit()

