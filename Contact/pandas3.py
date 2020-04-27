from pandas import Series, DataFrame

raw_data = {'open': [1, 2, 3, 4],
            'high': [10, 20, 30, 40],
            'close': [100, 200, 300, 400],
            'low': [2, 3, 4, 5]}

data = DataFrame(raw_data, columns=['open', 'high', 'low', 'close'],
                 index=['20.02.29', '20.03.01', '20.03.02', '20.03.03'])

print(data)
print(data['high']['20.02.29'])

print('\n')

print(data['low'])
print(data.loc['20.03.01'])

for co in data.columns:
    print(co)

for raw in data.index:
    print(raw)
