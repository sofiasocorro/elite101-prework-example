''' PROBLEM 1: PALINDROME CHECKER
Create a program that checks whether a given string is a palindrome.

Ignore spaces, punctuation, and capitalization when determining if the string reads the same forward and backward.
Handle edge cases, including empty strings and mixed characters.
Follow the UCASE strategy to structure your approach.'''

#WELCOME USER
print("Welcome to Sol's Palindrome Checker! \n")


#LOOP TO CHECK MULTIPLE TIMES
while True:
    #USER INPUT
    user_input = input("Enter text: ")
    #MAKES SURE INPUT DOESN'T CONSIDER SPACES OR CAPITALIZATION
    revised_output = user_input.replace (" ", "").lower()
    #CHECKS FOR PALIDROME
    reverse_input = revised_output [::-1]
    
    #OUTPUT: PALINDROME OR NOT
    if revised_output == reverse_input:
        print("The text you entered is a palindrome!\n")
    else:
        print("The text you entered is not a palindrome.\n")