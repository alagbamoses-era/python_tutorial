#!/usr/bin/python3


def main():
    print('You are in for this game')
    game_number = 10
    far = 0
    while (far < 3):
        guess_number = int(input('Enter a number between 1 and 20: '))

        if (guess_number <= 20):
     
            if (guess_number == game_number):
                print('You are correct')
                play_again = input('\n\nWill you like to play again? type (yes or no): ').lower()
                if play_again == 'yes':
                    continue
                elif play_again == 'no':
                    break
                else:
                    break
            else:
                print('Sorry, you can try again.')
                far += 1
        else:
            break
## Run the program
if __name__ == '__main__':
    main()



