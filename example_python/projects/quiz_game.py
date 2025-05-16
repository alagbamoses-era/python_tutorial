#!/usr/bin/python3

class ComputerQuestions:
    def __init__(self):
        pass

    def questions(self):
        print('You are welcome to my Computer Questions')

        playing = input('Are you ready to play? ').lower()

        if playing != 'yes':
            print('May be next time')
            quit()
        print("I hope you enjoy this game. Let's play the game")

        total_score = 4
        score = 0

        answer = input('What does CPU stands for? ').lower()
        if answer == 'central processing unit':
            print('correct!')
            score = score + 1
        else:
            print('Incorrect!')
        
        
        answer = input('What does GPU stands for? ').lower()
        if answer == 'graphic processing unit':
            print('correct!')
            score = score + 1
        else:
            print('Incorrect!')



        answer = input('What does RAM stands for? ').lower()
        if answer == 'random access memory':
            print('correct!')
            score = score + 1
        else:
            print('Incorrect!')



        answer = input('What does PSU stands for? ').lower()
        if answer == 'power supply':
            print('correct!')
            score = score + 1
        else:
            print('Incorrect!')


        print(f"You answered {score} correctly")
        print("You finally scored " + str((score/total_score) * 100) + "%.") 

ans = ComputerQuestions()
ans.questions()



