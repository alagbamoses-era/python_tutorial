#!/usr/bin/python3


def customers():
    customer_name = str(input('Enter your full name: '))
    mobile_number = str(input('Enter mobile number: '))
    year_of_birth = int(input('Enter year of birth: '))
    age = 2023 - year_of_birth
    current_city = str(input('Enter your current city: '))
    email = str(input('Enter your email: '))

    if age > 21:
        print(f'\nHello {customer_name}, your  mobile number is {mobile_number} you are {age} years old.You live in {current_city} your registered email is {email}\n') 
    return

customers()

def restaurant_capacity():
    length = int(input('Enter the lenght of the land area in cm: '))/100
    width = int(input('Enter the width of the land area in cm: '))/100

    area = length * width
    no_of_persons = int(area / 1.3)
    print('\nThe total number of persons to be accommodated is: ', no_of_persons)
    if no_of_persons > 70:
        print('\nSorry, a maximum of 70 persons are allowed')
    return

restaurant_capacity()


def weekend_sales():
    weekend = ['Friday', 'Saturday', 'Sunday']
    current_weekend_sales = int(input('What is current weekend sales? '))
    current_number_people_visited = int(input('How many people currently visited? '))
    last_weekend_sales = int(input('What was last weekend sales? '))
    last_number_people_visited = int(input('How many people visited last weekend? '))

    current_weekend_per_person_sale = current_weekend_sales / current_number_people_visited
    last_weekend_per_person_sale = last_weekend_sales / last_number_people_visited
    

    print(f"Current weekend's person average sale is {current_weekend_per_person_sale} and Last weekend's per person average sale is {last_weekend_per_person_sale}")
    return

weekend_sales()


def calculate_amount_and_change():
    invoice_number = str(input('Enter invoice number: '))
    total_amount = float(input('Enter Total invoice amount (in Dollars)'))
    amount_of_tip = float(input('Enter amount of tip: '))

    return 
