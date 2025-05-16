#!/usr/bin/python3

with open('seek7.txt', 'a+', encoding = 'utf-8') as file:
    file.write('This is how seek works')
    print('After write, position: ', file.tell())
    file.seek(0)
    print('Current position: ', file.tell())
    read_file = file.read(22)
    
    file.write('Python!')

    file.seek(8)
    file.write(read_file)

