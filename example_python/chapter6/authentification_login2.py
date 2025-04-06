#!/usr/bin/python3


## Empty dictionary to store user
users = {}

# Register a new user
def register():
    username = input('Enter a new username: ')

    if username in users:
        print('username already exists! Try another.')
        return

    password = input('Enter a password: ')
    role = input('Enter role (admin/user/guest): ').lower()

    if role not in ['admin', 'user', 'guest']:
        print("Invalid role! Defaulting to 'guest'.")
        role = 'guest'
    
    users[username] = {'password' :password, 'role':role}
    print('User registered successfully!\n')


# Function to login a user

def login():
    username = input('Enter username: ')
    password = input('Enter password: ')

    if username in users:
        if users[username]['password'] == password:
            print('Login successfully')

            # nested if-else for role-based access
            if users[username]['role'] == 'admin':
                print('Welcome, Admin! You have full access.')
            elif users[username]['role'] == 'user':
                print('Welcome, User! You have limited access.')
            else:
                print('Welcome, Guest! You have linited access.')
        else:
            print('Incorrect password. Access denied.')
    else:
        print('Username not found. Please register first.')


# Main function to provide new options

def main():
    while True:
        print('\n1. Register')
        print('2. Login')
        print('3. Exit')

        choice = input('choose an option: ')

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print('Good bye')
            break
        else:
            print('Invalid choice. Try again.')

# Run the program
if __name__ == '__main__':
    main()
        
