#!/usr/bin/python3


student_names = {}
#all_students_min = 0
#all_students_max = 3
# register a new student

def register():
    print('\nThis portal is now opened for student registration\n')
    #while all_students_min < all_students_max:
    
    number_of_students_to_register = int(input('How many students do you want to registeres: '))

    counter = 0
    while counter < number_of_students_to_register:
        class_ = input('Enter class: ')
        name = input('Enter full name: ')
        gender = input('Enter gender: ')

        print('\n')

        student_names[class_] = {
                'name':name, 
                'gender':gender
        }



        counter = counter + 1
        
    else:
        print('Registration is done fully')

    #print(student_names)

   # student_info = 0
   # student_max_info = 3
   # while student_info < student_max_info:
    #    key2 = input('Enter key: ').lower()
    #    value2 = input('Enter value: ').lower()
     #   students[key2] = value2
      #  students['names'] = student_names
       # print(students)
        #student_info = student_info + 1
        
    #else:
     #   print('Here are all students: ', students)
    

#print(register())


def view_register_logs():
    print('\nREGISTERED STUDENTS\n')
    #surname_login = input('Enter student surname: ').lower()
    #first_login = input('Enter student first name: ').lower()
    #middle_login = input('Enter students middle name: ').lower()
        
    for class_, info in student_names.items():
        print(f"{class_}, name: {info['name']}, gender: {info['gender']}")

def main():
    while True:
        print('\t\t ### MENU ###')
        print('\n\t\t1. Register')
        print('\t\t2. View Registered Logs')
        print('\t\t3. Exit')

        choice = input('Choose an option: ')

        if choice == '1':
            register()
        elif choice == '2':
            view_register_logs()
        elif choice == '3':
            break
        else:
            print('Invalid choice. Try again.')

# Run the program

if __name__ == '__main__':
    main()














