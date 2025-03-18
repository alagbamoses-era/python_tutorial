#!/usr/bin/python3

print("My name is %s and I am %d years old" %('Jon', 21))

print('This is letter %c' %('a'))

print("I've got %i eggs" %(333))

print("I have %u bananas" %(-5))

print("The temperature is %f degrees celcius" %(3.5))

print('My phone is %X new' %(10))

print('My %o' %(16))

## Using default order
students1 = "{}, {} and {}".format('John', 'Mary', 'Bill')
print("\nStudents by Default Order")
print(students1)


###Using Positional order

students2 = "{1}, {0} and {2}".format('John', 'Mary', 'Bill')
print("\nStudents by Positional Order")

print(students2)

### Using Keyword argument

students3 = "{m}, {b} and {j}".format(j='John', m='Mary', b='Bill')
print("\nStudents by Keyword Order")
print(students3)


