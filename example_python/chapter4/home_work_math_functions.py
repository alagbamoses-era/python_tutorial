#!/usr/bin/python3

import math

x1 = 5; x2 = 7; x3 = 4.251; x4 = 10

# maximum

print('Maximum value: ',max( x1, x2, x3, x4))
# Minimum

print('Minum value: ',min( x1, x2, x3, x4))

print('modf: ', math.modf(x3))

### power

print('7 raise to power of 5: ', pow(x2, x1))


# Rounding up of decimal places

print('Approximate 4.251 to 1 dp: ', round(x3, 1))

# Square root

print('Square root of 5: ', math.sqrt(x1))



## OPERATORS

first_name = 'Moses'
last_name = 'Alagba'

###Concatenation

full_name = first_name + '  ' + last_name
print('My full name is ', full_name)

## Iteration
print('My First name in 3 places ', first_name*3)

### slice
print('First 3 letters of my first name :', first_name[:3])


### Range slice

print('Between 2nd and 4th letter of my first name: ',first_name[1:4])


### In (Membership)
print('letter M is in my first name: ',  'M' in first_name)


## not in (membership)
print('Letter O is not in my last name: ', 'O' not in last_name)


## r/R (raw string)


raw_string = r"hello \world"
regular_string = "hello \world"
print(raw_string)
print(regular_string)

print("He asked, \"what's that doing here?\"")
print('''He asked, "what's that doing here?" ''') 

