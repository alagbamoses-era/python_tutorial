#!/usr/bin/python3

class Email:
    def __init__(self):
        self.email = input('Enter your email: ')
        self.username = self.email[:self.email.index('@')]
        self.domain = self.email[self.email.index('@') + 1 :]

        #return (f' Username is {username} and domain is {domain}')

    def save(self):
        with open('email.txt', 'a+') as file:
            info = f'{self.username} : {self.domain}\n ' 
            file.write(info)

email = Email()
email.save()

