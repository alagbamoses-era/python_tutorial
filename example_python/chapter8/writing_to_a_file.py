#!/usr/bin/python3

#file = open('myfile.txt', 'w')
#file.write("The purple cow poem is a short nonsense poem first published in 1895 written by American writer Gelett Burgess");
#file.close()


text = open('myfile.txt', 'r+')

mytext = text.read(120);
print(mytext)

text.close() ### giving allocating space back to the computer
