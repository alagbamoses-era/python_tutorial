#!/usr/bin/python3

# from math import random
#game_num = random.choice(min_num, max_num)



def main():
    game_num = 7
    no_of_times = 0
    min_num = 1
    max_num = 50
    while (no_of_times < 3):
        no_of_times += 1
        guess_num = int(input('Guess a number: '))

        if (min_num <= guess_num <= max_num):
            print(f'Your guess is {guess_num}')
        

            if (guess_num == game_num):
                print(f'Congratulation! you guessed {guess_num} which is correct')
        
                play_again = input('\n\nDo you want to play again? type yes or no: ').lower()
                if play_again == 'yes':
                    continue
                elif play_again == 'no':
                    break
                else:
                    break
            elif (guess_num > game_num):
                print(f'{guess_num} is too high')
        
    
            else:
                print(f'{guess_num} is too low')
        
        else:
            print('Enter number 1 to 50')


##run the program
if __name__ == '__main__':
    main()


