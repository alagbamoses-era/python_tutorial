#!/usr/bin/python3 


list_ = ['one', 'two', 'three\n']
f = open('writeline.txt', 'w')
list_string = ' '.join(list_)
f.write(list_string)
f.close()

list_list = ['one', 'two', 'three', '4']
f1 = open('wt.txt', 'w')
new_list = list(list_)
print(new_list)
f1.writelines(new_list + '\n' for new_list in new_list)
f1.close()
