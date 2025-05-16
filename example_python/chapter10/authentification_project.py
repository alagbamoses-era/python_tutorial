#!/usr/bin/python3


import sys

class Authentification:
    def __init__(self):
        self.users = {}
    

    def register(self):
        self.users = {}
        
        
        role = str(input('Enter role (admin/user/guest: \
                ')).lower()
        
        if role in ['admin', 'user', 'guest']:
            username = str(input('Enter a new username: '))       
            password = str(input('Enter a password: '))

            self.users[username] = password     

            Text()
            print(f'{role} registered successfully\n')
            print(self.users)

            return

        elif role not in ['admin', 'user', 'guest']:
            
            print('Default to {role}')
            username = str(input('Enter a new username: '))       
            password = str(input('Enter a password: '))
            self.users[username] = password
            Text()
            print(f'{role} registered successfully\n')
            return


        else:
            return
        

class Text(Authentification):
    def db(self):
        with open('database.txt', 'a+') as file:
            for username, password in users.items():
                file.write(f'{username}:{password}\n')



class Login(Authentification):
    def login_account(self):
        self.username = str(input('Enter username: '))
        self.password = str(input('Enter password: '))

        
        if self.username in self.users:
            if self.password == self.password:
                print('Login successfully')

                if self.users[role]  == 'admin':
                    print('Welcome, Admin! You have full \
                            access')
                elif self.users[role]  == 'user':
                    print('Welcome, User! You have limited \
                            access. ')
                else:
                    print('Welcome, Guest! You have limited \
                            access')
            else:
                print('Incorrect password. Access denied')
        else:
            print('Username not found. Please register first.')


class Start(Authentification):
    def main(self):
        while True:
            print('\n1. Register')
            print('2. Login')
            print('3. Exit')

            choice = input('Choose an option: ')

            if choice == '1':
                super().register()
            elif choice == '2':
                Login.login_account(self)
            elif choice == '3':
                print('Good bye')
                super().db()
                sys.exit()
            else:
                print('Invalid choice. Try again')

if __name__ == '__main__':
    start = Start()
    start.main()



