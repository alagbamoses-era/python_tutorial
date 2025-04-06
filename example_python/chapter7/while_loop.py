#!/usr/bin/python3


x = int(input('Enter a value for x: '))
sum = 0
i = 1
while i <= x:
    sum = sum +1
    print(sum)
    i = i + 1 # update counter
print('The total sum is ', sum)

# Infinite loop

while True:
    print('Forever')
    break

list_ = [1, 2, 3, 4, 5]

while list:
    print('list value pop out: ', list_.pop())





