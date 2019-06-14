import random
print('''
Password Generator
==================
''')
#Ask the user how many passwords they would like and ask the length
number = input('How many passwords would you like? ')
number = int(number)

len = input('Enter the length of your password: ')
len = int(len)

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,_-!@$&'

print('\nSuggested Passwords: ')

#For loop to generate passwords in given range 
for pwd in range(number):
    password = ' '
    for c in range(len):
        password += random.choice(characters)
    print(password)
     
