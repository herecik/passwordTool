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
        print("Insert parameters so i know what to do. You can use command --help")
    elif(state == 1):
        print("Other error")

def operation():
        if(sys.argv[1] == "--help"):
            help_prompt()
        elif(sys.argv[1] == "--controll"):
            controll_password()
        elif(sys.argv[1] == "--generate"):
            generate_password()
        else:
            error_prompt(0)


def check_args():
    if(len(sys.argv) < 2):
        error_prompt(0)
        exit(1)

operation()
check_args()


