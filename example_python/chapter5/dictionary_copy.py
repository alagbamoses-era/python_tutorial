#!/usr/bin/python3


### dict.copy

dict_student = {'name':'Jack', 'age':20, 'weight':60, 'height':170}

dict_student_copy = dict_student.copy()

print(dict_student_copy)

###   dict.fromkeys()

list_food = ['rice', 'beans', 'meat', 'drinks']
list_qty = '50 bags'

dict_food = dict.fromkeys(list_food, list_qty)
print(dict_food)


### Using zip function

list_keys = ['name', 'gender', 'occupation', 'salary', 'city']

all_values = ['Jack', 'Male', 'programmer', 100000, 'London']



## dict_values = dict.fromkeys(list_keys, all_values)


dict_values = {k:v for k, v in zip(list_keys, all_values)}
print('first option: ', dict_values)




### dict.get(x, default=none)

dict_books = {'book1':'python', 'book2':'java', 'book3':'c'}

dict_book2 = {'book4':'javascript', 'book5':'r'}


book1 = dict_books.get('book1')
print(book1)


print(dict_books.get('book4', 'not found'))

### dict.has_key(x)

if 'book1' in dict_books:
    print('key exists')
else:
    print('key does not exist')

if 'book5' in dict_books:
    print('key exists')
else:
    print('key does not exist')


### dict.items


print(dict_books.items())

dict_items = dict_books.items()
list_items = list(dict_items)
print(list_items)

for key, value in dict_books.items():
    print(f'{key}:{value}')


#### dict.keys()

print(dict_books.keys())

dict_join = dict_books.keys()
list_join = list(dict_join)
print(', '.join(list_join))


#### dict.setdefault(x, default = none)


print(dict_books.setdefault('book1', 'not found'))



#### dict.update(dict2)

dict_books.update(dict_book2)


print(dict_books)



#### dict.values()

print(dict_books.values())


dict_books_values = dict_books.values()

list_values = list(dict_books_values)

print(', '.join(list_values))


