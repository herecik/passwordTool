import sys
from sub_controll import *
from sub_generate import *

parametres = ["capital", "non", "numbers", "4"]

def help_prompt():
    print("Choose controll or generate as a program argument to generate new password or to controll your password")

def controll_password():
    current_password = get_password()
    check_password(current_password)

def generate_password():
    password = get_parameters(parametres)
    print("Your new 100% secure password is: " + password)

def error_prompt(state):
    if(state == 0):
        print("Insert program parameters so i know what to do. You can use command --help")
    elif(state == 1):
        print("Bad program parametres. Type --help for help lol.")
    elif(state == 2):
        print("unknown error")

def operation():
    if(len(sys.argv) > 1):
        if(sys.argv[1] == "--help"):
            return "help"
            #help_prompt()
        elif(sys.argv[1] == "--controll"):
            return "controll"
            #controll_password()
        elif(sys.argv[1] == "--generate"):
            #generate_password()
            return "generate"
        else:
            error_prompt(0)
    else:
        error_prompt(0)

def launch_modules(module):
    if(module == "help"):
        help_prompt()
    elif(module == "controll"):
        controll_password()
    elif(module == "generate"):
        generate_password()
    else:
        error_prompt(2)

module_sellected = operation()
launch_modules(module_sellected)

