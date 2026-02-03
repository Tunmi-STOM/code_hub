# IMPORT - TOOLBOX 
import secrets
import string
import time

# ----------------------------------------------
# Create a function to return a string at random
# ----------------------------------------------

# Define a function that will ask to Generate a string (The Logic)
def random_string(length=16, include_chars=False, random_spaces=False):
    characters = string.ascii_letters + string.digits 
    if include_chars:
        characters += string.punctuation
    if random_spaces:
        characters += " "
        
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password
    
def home():
    print("String Generator\n1. Generate Random string (Default)\n2. Custom String Generation")
    options = input()
        
    if options == '1':
        app()
    elif options == '2':
        edit_parameters()
            
            
def edit_parameters():
    length = int(input("Enter the number of chars: "))
    include_chars = input("Include special chars? (y/n): ")
    include_spaces = input("Include spaces? (y/n): ")
       
    if include_chars == 'y':
        chars = True
    elif include_chars == 'n':
        chars = False
    else:
        chars = False
        time.sleep(0.5)
        print("Invalid Input for special chars (Default value selected)")
        time.sleep(0.5)
           
    if include_spaces == 'y':
        spaces = True
    elif include_spaces == 'n':
        spaces = False
    else:
        spaces = False
        print("Invalid Input for spaces (Default value selected)")
        time.sleep(0.5)
        
    time.sleep(0.5)
    print(f'\n\n{random_string(length, chars, spaces)}\n\n')
    home()
        
        
def app():
    generate = input("Generate string? (enter y/n)")
    if generate == 'y':
        # wait for 1.5 secs
        time.sleep(1.5)
        print(f'\n\n{random_string()}\n\n')
        app()
    elif generate == 'n':
        print('trying again...')
        # wait for 1.5 secs
        time.sleep(1.5)
        app()
    else:
        print('Invalid input.')
        close = input('Close str generator? (enter y/n)')
        if close == 'y':
            print('Closed')
        elif close == 'n':
            home()
        else:
            print('Something went wrong')


try:
    home()
    
except:
    print("An error occured")