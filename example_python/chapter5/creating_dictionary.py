#!/usr/bin/python3

empty_dict = {}

integerkey_dict = {1:'Mango', 2:'Apple', 3:'Orange'}

mixedkey_dict = {'name':'John', 0:[2, 4, 3]}

print(integerkey_dict[1])
print(integerkey_dict[2])
print(integerkey_dict[3])

print(mixedkey_dict.get('name'))
print(mixedkey_dict.get(0))


list_dict = {'name':['Moses', 'Alagba', 'Pen'],\
        'city':('Newcastle', 'Crewe', 'London',)} 

name_list = list_dict.get('name')
city_tuple = list_dict.get('city')

name_list2 = []
city_tuple2 = ()

name_list2.extend(name_list)
city_tuple3 = city_tuple2 + city_tuple 

print(name_list)
print(city_tuple)

print(name_list2)
print(city_tuple3)


