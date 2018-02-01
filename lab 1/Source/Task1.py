import re                               #importing regular expression module.

print('UMKC Web login\n')

while True:                             # while loop started and run until it is false
    inp = input('\nEnter a valid password:')        #user input for a password

    if (len(inp) < 6 or len(inp) > 16):         #checking length of user input
        print('Password should be between 6 and 16 characters.')
    elif re.search('[0-9]', inp) is None:           #searching 0-9 in the user input
        print('Password should have atleast one number')
    elif re.search('[A-Z]', inp) is None:           #searching for upper case characters in user input
        print('Password should have one upper case character')
    elif re.search('[a-z]', inp) is None:           #searching for lower case characters in user input
        print('Password should have one lower case character')
    elif re.search('[$,@,!,*]', inp) is None:       #searching for special characters  in user input
        print('Password should have one special character')
    else:
        print('\nPassword accepted!')
        break                                       #end of loop