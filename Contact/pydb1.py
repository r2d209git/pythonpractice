from pandas import Series, DataFrame
import pandas as pd
import sqlite3


raw_data = {"col0" : [1, 2, 3, 4],
            "col1" : [10, 20, 30, 40],
            "col2" : [100, 200, 300, 400]}

df = DataFrame(raw_data)

print(df)

con = sqlite3.connect("D:\\Python\\prj\\Contact\\db\\kospi.db")

# WRITE PART
"""column, row(index)로 이뤄진 DB Table의 구조 자체가 Pandas의 DataFrame 객체 구조와 동일하느로 sqlite와 direct 연동에 유용"""
df.to_sql('test', con, chunksize=1000, if_exists='replace')  #'test'는 Table name #chunksize = 한번에 기록하는 row 수 제약



# READ PART
cursor = con.cursor()
cursor.execute("SELECT * from test")
test = cursor.fetchall()
"""2차원 list matrix type * column과 index가 제외되므로"""
print(type(test))

print(test[0][2])

"""index_col : index로 사용될 column 지정이며 default는 None이면 0부터 시작하는 index 할당됨"""
df2 = pd.read_sql("SELECT * from test", con, index_col=None)
print(df2)

"""index_col : index로 사용될 column 지정"""
df3 = pd.read_sql("SELECT * from test", con, index_col='index')
print(df3)

con.commit()
con.close()

