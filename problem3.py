
''' PROBLEM 3: UNIQUE CHARACTERS CHECKER
Create a program that checks whether all characters in a given string are unique.'''


#WELCOME USER
print('Welcome to Unique Characters Checker!\n')
while True:
    #CHECKER
    user_input = input('Please enter a word: ')
    #REMOVES SPACES AND CONVERTS TO CASE INSENSITIVE
    no_spaces = user_input.replace (" ", "").lower()
    
    #UNIQUE CHARACTERS
    unique_chars = set(no_spaces)

    if len(no_spaces) == len(unique_chars):
        print('True\n')
    else:
        print('False\n')

    

