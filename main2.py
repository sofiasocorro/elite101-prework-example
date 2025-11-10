'''

CHATBOT: ELITE'S BANKING SYSTEM


'''


#WELCOME USER
print(''''

-------------------------

Welcome to Elite's Bank!
      
-------------------------
      
''')

#USER'S NAME
name = input("Please enter your name: ")
age = input('Greetings ' + name + '! how old are you? ')
print('Welcome ' + name + '!' ' I remember when I was ' + age+ ', How can I help you today? \n')

#USER'S CHOICE
def choices():
    print('''
    -------------------------

    Please choose from the following:
    1. Check balance
    2. Add money
    3. Transfer money
    4. Exit 
        
    -------------------------
    ''')

#SET GENERAL/SAVINGS BALANCE
general_balance = 1500
savings_balance = 500

def check_balance():
    print('General balance: $', general_balance)
    print('Savings balance: $', savings_balance)


def add_balance():
    account_choose = input('Which account do you want to add money to? General or savings: ' )
    revised_choice = account_choose.lower()

    if revised_choice == 'general':
        add_amount = input('How much money do you want to add to your general account? $')
        add_amount = float(add_amount)
        new_general_balance = general_balance + add_amount
        print('New general balance: $', new_general_balance)

    elif revised_choice == 'savings':
        add_amount = input('How much money do you want to add to your savings account? $')
        add_amount = float(add_amount)
        new_savings_balance = savings_balance + add_amount
        print('New savings balance: $', new_savings_balance)
       
    else:
        correct_choice = input('Please choose between general or savings: ')



def transfer_balance():
    account_choose = input('Which account do you want to transfer money to? General or savings: ' )
    revised_choice = account_choose.lower()

    if revised_choice == 'general':
        transfer_amount = input('How much money do you want to transfer to your general account from savings? $')
        transfer_amount = float(transfer_amount)
        new_savings_balance = savings_balance - transfer_amount
        new_general_balance = general_balance + transfer_amount
        print('New general balance: $', new_general_balance)
        print('New savings balance: $', new_savings_balance)
                

    elif revised_choice == 'savings':
        transfer_amount = input('How much money do you want to transfer to your savings account from general? $')
        transfer_amount = float(transfer_amount)
        new_savings_balance = savings_balance + transfer_amount
        new_general_balance = general_balance - transfer_amount
        print('New general balance: $', new_general_balance)
        print('New savings balance: $', new_savings_balance)

    else:
        correct_choice = input('Please only choose between general or savings: ')    


def exit_bank():
    print('Goodbye, ' + name+ '! Have a great day!')
    


while True:
    choices()
    choice = input('Please enter your choice: ')

    if choice == '1': 
        check_balance()


    elif choice == '2':
        add_balance()
            
     
    elif choice == '3':
        transfer_balance()

    elif choice == '4':
        exit_bank()
    

    else:
        fix = input('Sorry, please only choose: 1, 2, 3, or 4 ')



  
