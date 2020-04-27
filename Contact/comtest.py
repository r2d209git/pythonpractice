import win32com.client

excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True

wb = excel.Workbooks.Add()
ws = wb.Worksheets("Sheet1")

ws.Cells(1, 1).Value = "김수진 사랑해!"

wb.SaveAs('D:\\Python\\prj\\learnpython\\file\\exceltest.xlsx')

excel.Quit()
