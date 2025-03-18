#!/usr/bin/python3

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

year_list = [2017, 'Two Thousand and seventeen', 'XXVII', 20.17]

favorites = ['a', 'x', 't', 'xx']

print(', '.join(weekdays))
print(', '.join(map(str, year_list)))
print(', '.join(favorites))
