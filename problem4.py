'''PROBLEM #4: GUESSING GAME
Create a CLI program that plays a guessing game with the user.
Randomly select a number between 1 and 100 when the game starts.
Prompt the user for guesses until they find the number.
Tell the user whether their guess is too high or too low, and allow repeated attempts.
Congratulate the player and exit when the guess is correct.
Handle invalid inputs gracefully (non-numeric values or numbers outside the range).
'''
import random
#WELCOME USER
print("\nWelcome to Sol's Guessing Game!\n")

#RANDOM NUMBER GENERATOR
random_number = random.randint(1, 100)

while True:
    select_number = input('Please select a number between 1 and 100: ')
    select_number = float(select_number)

    #INVALID INPUT 
    if select_number < 1 or select_number > 100:
        print('\nInvalid input! Please select a number between 1 and 100 \n')
        
    #IF USER'S GUESS IS TOO HIGH
    if select_number >= random_number:
        print('Too High!')

    #IF USER'S GUESS IS LOW   
    if select_number <= random_number:
        print('Too low!')

    #IF USER'S GUESS = CODE'S RANDOM NUMBER 
    if select_number == random_number:
        print('Congrats, you guessed the right number! \n')
        break



