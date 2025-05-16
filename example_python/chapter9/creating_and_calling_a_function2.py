#!/usr/bin/python3

def greeting(name):
    """This function greets the user
    when the person's name is passed in as a parameter"""

    print("Greeting, ", name + '!')

username = str(input('Enter your name: '))
greeting(username)


