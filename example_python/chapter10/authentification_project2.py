#!/usr/bin/python3


import sys

class Authentication:
    def __init__(self):
       self.users = {}
    

    def register(self):

        self.role = str(input('Enter role (admin/user/guest: ')).lower()
              
        
        self.username = str(input('Enter a new username: '))
        self.password = str(input('Enter a password: '))
        self.users[self.role] = {self.username : self.password}
        
        if self.role in ['admin', 'user', 'guest']:
          
            
            if self.role in self.users:
                print('key found')
            else:
                print('key     not found')     


            print(self.role)
            print(self.users)
            print(f'{self.role} registered successfully\n')
            

            return

        elif self.role not in ['admin', 'user', 'guest']:
            
            print('Default to {self.role}')
            self.username = str(input('Enter a new username: '))       
            self.password = str(input('Enter a password: '))
            self.users[username] = password
            Text()
            print(self.users)
            print(f'{self.role} registered successfully\n')
            
            return


        else:
            return
        

    def db(self):
        with open('database.txt', 'a+') as file:
            role_ = self.users[self.role]
            for self.username, self.password in role_.items():

                file.write(f'{self.username}:{self.password}\n')



class Login(Authentication):
    def login_account(self):
        self.username = str(input('Enter username: '))
        self.password = str(input('Enter password: '))

        
        if self.username in self.users[self.role]:
            if self.password == self.password:
                print('Login successfully')

                if self.role  == 'admin':
                    print('Welcome, Admin! You have full access')
                elif self.role  == 'user':
                    print('Welcome, User! You have limited \
                            access. ')
                elif self.role == 'guest':
                    print('Welcome, Guest! You have limited access')
                else:
                    print('Invalid')
            else:
                print('Incorrect password. Access denied')
        else:
            print('Username not found. Please register first.')


class Start(Authentication):
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



