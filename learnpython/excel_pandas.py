#reference : https://towardsdatascience.com/learn-how-to-easily-do-3-advanced-excel-tasks-in-python-925a6b7dd081
import pandas as pd

if __name__ == "__main__":
    sales = pd.read_excel('https://github.com/datagy/mediumdata/raw/master/pythonexcel.xlsx', sheet_name = 'sales')
    states = pd.read_excel('https://github.com/datagy/mediumdata/raw/master/pythonexcel.xlsx', sheet_name = 'states')
    print(sales.head())
    sales['MoreThan500'] = ['Yes' if x > 500 else 'No' for x in sales['Sales']]
    # print(sales['MoreThan500'])

#VLOOKUP = 두개의 excel sheet를 같은 column 값을 key로 매핑해 left merge
    sales = pd.merge(sales, states, how='left', on='City')
    print(sales.head())

#pivot
    pivoted = sales.pivot_table(index = 'City', values = 'Sales', aggfunc = 'sum')
    print(pivoted.head())