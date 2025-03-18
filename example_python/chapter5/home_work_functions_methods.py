#!/usr/bin/python3


### Function
print('This is my home work. \nI have used two functions which are: \
        "Minimum" and "Maximum". \nI have also use two methods which are: \
        "Reverse" and "Sort". ')
age_employees = [ 20, 50, 65, 45, 50, 40, 35, 39, 60, 48] # Age of employees

print('Minimum age: \t', min(age_employees), 'years')
print('Maximum age: \t', max(age_employees), 'years')



### Methods

age_employees.reverse()
print('Reverse age of the employees: \t', ', '.join(map(str, age_employees)))

age_employees.sort()
print('Sort the age of the employees: \t', ', '.join(map(str, age_employees)))


list_x = [ 1, 2, 3] ; list_y = [4, 5, 6]

list_x.extend(list_y)

print(list_x)

list_x.insert(2, list_y)
print(list_x)

list_x.pop(list_x[-1])
print(list_x)


list_x.pop(list_x[3])
print(list_x)


