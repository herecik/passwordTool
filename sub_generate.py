
def numeric_input_check(input):
    try:
        int(input)
    except:
        print("Input error. Choose only inteegers.")
        exit(1)

def generate_rand():
    return "asd2585ds"

def generate_spec():
    return "specspec558"

def check_conditions(parametres):
    total = int(parametres[0])
    cap = int(parametres[1])
    ncap = int(parametres[2])
    num = int(parametres[3])
    fit = cap + ncap + num
    if(total < fit):
        print("Your password is too short for your demands")
        exit(1)

def get_parameters(parametres):
    y = input("Do you want specify your password? [y/n]: ")

    if(y == "y"):
        parametres[0] = input("Choose lenght of your password: ")
        parametres[1] = input("Choose how many capital letter in password: ")
        parametres[2] = input("Choose how many non-capital letter in password: ")
        parametres[3] = input("Choose how many numbers in password: ")
        for x in parametres:
            numeric_input_check(x)

        check_conditions(parametres)
        new_password = generate_spec()
        return new_password
    else:
        new_password = generate_rand()
        return new_password
           





