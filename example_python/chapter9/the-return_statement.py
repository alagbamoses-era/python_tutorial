#!/usr/bin/python3


def agegroup_checker(age):
    """This function returns the
    user's age groip name based on the age entered."""

    if age >= 18:
        agegroup = 'Adult'
    elif age >= 13:
        agegroup = 'Teenager'
    elif age >= 0:
        agegroup = 'Child'
    else:
        agegroup = 'Invalid'

    return (agegroup)

age = int(input('Enter your age to check age agroup: '))

print('Your age group is: ', agegroup_checker(age))


