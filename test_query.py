__author__ = 'Kavin'
__usage__ = ''

import sys

columns = ['haha', 'hihi', 'hehe']
values = ['1', '2', '3']

query = 'INSERT into table (%s) VALUES (%s);' % (', '.join(columns), ', '.join(values))

print(query)
