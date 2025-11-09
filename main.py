print('Welcome to Elite 101 Chatbot!')
name = input("Please enter your name: ")
age = input('Greetings ' + name + '! how old are you? ')
print('Welcome ' + name + '!' ' I remember when I was ' + age+ ', How can I help you today? \n')
print('''Please choose from the following:
1. Create an account
2. Generate a table
3. Sort numbers
4. Exit ''')

while True:
    choice = input('Please enter your choice: ')
    if choice == '1':
        print('Great')

    if choice == '2':
        print('generates table')

    if choice == '3':
        print('sorts number')

    if choice == '4':
        print('Goodbye, ' + name+ '! Have a great day!')
        break
    else:
        fix = input('Please type 1, 2, 3, or 4: ')

# add more details
    