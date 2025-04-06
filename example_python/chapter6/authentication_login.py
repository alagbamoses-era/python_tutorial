#!/usr/bin/python3

users = {
        'admin': {'password': 'admin123', 'role': 'admin'},
        'user1': {'password': 'userpass', 'role': 'user'},
        'guest': {'password': 'guest', 'role': 'guest'}
}

# Get user input
username = input('Enter username: ')
password = input('Enter password: ')

# Check if the username exists

if username in users:
    # check if the password matches
    if users[username]['password'] == password:
        print('Login successful!')

        # Nested if-else to check the role
        if users[username]['role'] == 'admin':
            print('Wilcome, Admin! You have full access.')
        elif users[username]['role'] == 'user':
            print('Welcome, User! Yo have limited access.')
        else:
            print('Welcome, Guest! You ahve read-only access.')
    else:
        print('Incorrect password. Access denied.')

else:
    print('Username not found. Please register first.')



