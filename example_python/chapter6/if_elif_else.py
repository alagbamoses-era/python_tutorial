#!/usr/bin/python3

age = int(input('enter age to evaluate: '))

if (age >= 18):
    agegroup = 'Adult'
elif (age >= 13):
    agegroup = 'Teenager'
elif (age >= 0):
    agegroup = 'Child'
else:
    agegroup = 'Invalid'

print(agegroup)


### Weight exercise
print('\n\n')
bmi = float(input('What is your BMI: '))

if bmi >= 30:
    status = 'Obesity'
elif bmi >= 24.5:
    status = 'Over weight'
elif bmi >= 18.5:
    status = 'Normal'
else:
    status = 'Under weight'

print(status)


print('\n\n')
#### and , or, student results, 5 students, test 
## if 2 students , 90= pass , ist, 80 and above = second, 60 and above third , 50 and belo w= fail 

test = float(input('What is yout test score: '))

if (test >= 90):
    position = 'Pass with first position'
elif (test >= 80):
    position = 'Pass with second position'
elif (test >= 60):
    position = 'Pass with third position'
else:
    position = 'Try again next time'

print(position)





