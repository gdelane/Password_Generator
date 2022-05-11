 
# Hello! I'm Godwin, this is my first actual python project. I've tried to include comments to help explain the steps. 
#Hope you find it useful!


import random
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+-=[]/,.<>"

while 1:
    password_length = int(input("How many characters would you like your password to have? "))
    password_count  = int(input("How many passwords would you like to generate? "))
    for x in range(0, password_count):
        password = ""
        for x in range(0, password_length):
            password_characters = random.choice(characters) 
            password            = password + password_characters
        print("Here is your password: ", password)

# We imported the random module becuase the generator is going to be picking characters at random.
# The "characters" contain include the entire english alphabet in both upper and lower cases and a few special characters.
# We use 'while' to crate a loop.
# The desired password length that is inputed is stored as an integer value using the 'int()' in "password_length"
# "password_count" stores the number of passwords to be generated also as an integer value.
# The first "for x in range" creates a loop and gives a number for how many times the succeeding code should run. "(0, password_count)" means it runs as many times as the user wants a new password.
# The second  for loop gives how many characters the user wants in their password by using the "password_length".
# "password_characters" contains a random choice that the code selects from the characters on each iteration.
# However, the second line is needed to join together all the choices in each inerations as one string to make up the ppassword.
# So for each iteraion, "passwrod = password + password_characters" will add the previously selected character(s) to the present one until th desired password_length is reached.




