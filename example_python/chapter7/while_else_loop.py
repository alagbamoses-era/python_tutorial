#!/usr/bin/python3

loops = int(input('Enter the number of times to loop: '))

counter = 0
while counter < loops:
    counter = counter + 1
    print('Iteration so far: ', counter)
else:
    print('Maximum loops of ', counter)


### LIST

num = [10, 20, 30, 40, 50]

counter = 0
while counter < len(num):
    #counter = counter + 1
    print('list items: ', num[counter])
    counter = counter + 1
else:
    print('All is printed')


### empty list
empty_list = []

list_length = int(input('Enter list length: '))

counter = 0
while counter < list_length:
    values = int(input('input list element: '))
    empty_list.append(values)
    counter = counter + 1
else:
    print('\nList satisfied\n')


print('value is: ', empty_list)

### TUPLE

tuple_element = (10, 20, 30, 40,)
counter = 0
while counter < len(tuple_element):
    print('tuple value is: ', tuple_element[counter])
    counter = counter + 1
else:
    print('All is printed')


empty_new_list = []
new_list_length = int(input('Enter list length: '))

counter = 0
while counter < new_list_length:
    value = int(input('Enter value: '))
    empty_new_list.append(value)
    counter = counter + 1
else:
    print('All values added')

new_tuple = tuple(empty_new_list)
print(new_tuple)



#### Dictionary
dict_element = {}
dict_length = int(input('Enter dictionary length: '))

counter = 0
while counter < dict_length:
    key = input('Enter key: ')
    value = input('Enter value: ')
    dict_element[key] = value
    counter = counter + 1
else:
    print('All keys and values collected')

print(dict_element)


### set
empty_set = set()

set_length = int(input('Enter number of set length: '))

counter = 0
while counter < set_length:
    set_item = input('Enter the item: ')
    empty_set.add(set_item)
    counter = counter + 1
else:
    print('All set items collected')

print(empty_set)





