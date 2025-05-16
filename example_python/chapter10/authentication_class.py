#!/usr/bin/python3


import sys
import re

users = {}

class Authentication:

    password = None


    def __init__(self):
        counter = 0
        pass

    @classmethod
    def register(cls):
        username = str(input('Create username: '))
        cls.password = str(input('Create passeord: '))
        cls.password2 = str(input('Confirm password: '))

        
        if cls.password == cls.password2:

            if len(cls.password) > 5:
                if re.search(r'[A-Z]', cls.password) and re.search(r'[0-9]', cls.password) and re.search(r'[a-z]', cls.password) and re.search(r'[$%&^/@"]', cls.password):
                    print('Strong password')
                else:
                    print('weak password')
                    cls.register()
        else:
            print('Passowrds do not match, please restart')
            cls.register()    
        
        users[username] = cls.password
        #passwd = cls.password
        


    @classmethod
    def db(cls):
        with open('db.txt', 'a+') as file:

            for cls.username, cls.password in users.items():
                Authentication.counter =+ 1
                file.write(f'{Authentication.counter}, {cls.username}:{cls.password}\n')
                
            print('username and password now added')


class Login(Authentication):

    def __init__(self):
        pass  

def access():
    username = input('Enter username: ')
    password = input('Enter password: ')

    if username in users:
        print(users)
        #existing_password = Authentication()
            
        #print(f'{Authentication.password}')
        if password == Authentication.password:
            print('Login suceesfully')
        else:
            print('please try again')

    #def open_file(self):
        #with open('db.txt', 'r') as file_open:
            #file_password = input('Enter Password: ')
            #if save_password == file_password:
                #file.open.readlines()

class Start(Login):
    def main(self):
        while True:
            print('\n1. Register')
            print('2. Login')
            print('3. View File')
            print('4. Exit')

            self.choice = int(input('Enter option: '))

            if self.choice == 1:
                super().register()

            elif self.choice == 2:
                access()

            elif self.choice == 3:
                super().open_file()

            elif self.choice == 4:
                super().db()
                print('Good bye')
                break
            else:
                print('Invalid option')
                start.main()

if __name__ == '__main__':
    start = Start()
    start.main()

#Authentication.register()

#authen = Authentication()

#authen = Login()
#authen.register()
#authen.db()
#authen.access()



