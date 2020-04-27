from pandas import Series, DataFrame

raw_data = {'col0': [1, 2, 3, 4],
            'col1': [10, 20, 30, 40],
            'col2': [100, 200, 300, 400]}

data = DataFrame(raw_data)

print(raw_data)
print(data)

print('\n')

print(data['col0'])
print(type(data['col0']))
print(data['col0'][3])

