import random
import string
import time

#TODO special characters in password                        

def numeric_input_check(input):
    try:
        int(input)
    except:
        print("Input error. Choose only inteegers.")
        exit(1)

def check_len(input_password):
    if(len(input_password) < 8):
        print("You need to put more than 7 characters into your password.")
        exit(1)

#random new password generated with at least one uppe, one lower case and one digit
def generate_rand(size, chars = string.ascii_lowercase + string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size)) + "Ax" + time.strftime("%S")

def generate_spec(param):
    custom_password = "".join(random.choice(string.ascii_uppercase) for _ in range(int(param[0])))
    custom_password = custom_password + "".join(random.choice(string.ascii_lowercase) for _ in range(int(param[1])))
    custom_password = custom_password + "".join(random.choice(string.digits) for _ in range(int(param[2])))
    custom_password = "".join(random.sample(custom_password, len(custom_password)))

    return custom_password

def get_parameters(parametres):
    y = input("Do you want specify your password? [y/n]: ")

    if(y == "y"):
        
        parametres[0] = input("Choose how many capital letter in password: ")
        parametres[1] = input("Choose how many non-capital letter in password: ")
        parametres[2] = input("Choose how many numbers in password: ")
        for x in parametres:
            numeric_input_check(x)
                
        new_password = generate_spec(parametres)

        z = input("Do you want to add something special to the end of your password? [y/n]: ")
        if(z == "y"):
            parametres[3] = input("What do you want to put in: ")
            new_password = new_password + parametres[3]

        check_len(new_password)
        return new_password
    else:
        new_password = generate_rand(8)
        return new_password
           





