def get_password():
    password = input("Your password: ")
    return password

def check_password(password):
    upper = 0
    lower = 0
    number = 0

    for n in password:
        if(n.isupper() == True):
            upper = 1
        elif(n.islower() == True):
            lower = 1
        elif(n.isdigit() == True):
            number = 1

    if(len(password) > 7):
        if(upper == 1 and lower == 1 and number == 1):
            print("Password is good.")
            #TODO save password with username to database
        else:
            print("Your password isn't strong enough.")
    else:
        print("Your password have to be at least 8 characters long.")
