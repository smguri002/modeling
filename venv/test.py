import pprint
import pandas
import numpy


x = {'name': 'x','id': 1, 'Parents': ['Angelo','Susan']}
print(x.get('name'))
for key, value in x.items():
    if value== 'x':
        print('name found')