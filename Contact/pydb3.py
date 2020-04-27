import pandas as pd
import pandas_datareader.data as web
import datetime
import sqlite3

start = datetime.datetime(2020, 3, 1)
end = datetime.datetime(2020, 3, 31)
df = web.DataReader("078930.KS", "yahoo", start, end)

con = sqlite3.connect("D:\\Python\\prj\\Contact\\db\\kospi2.db")
df.to_sql('078930', con, if_exists='replace')

readed_df = pd.read_sql("SELECT * FROM '078930'", con, index_col = 'Date')
print(type(readed_df.values))

for item in readed_df.columns:
    print(item)

for item in readed_df.values:
    print(item)

print(readed_df)