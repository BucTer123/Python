def write(text):
    print(text)

def gets_column(variable):
    variable = input("> ")
    print(variable)

def string_variable(variable_string):
    question1 = input("Write ? :")

    if question1 == "y" or question1 == "Y":
        print(variable_string)
    else:
        exit(0)

def int_variable(variable_number):
    question2 = input("Write ? :")

    if question2 == "y" or question2 == "Y":
        print(variable_number)
    else:
        exit(0)

def float_variable(variable_number):
    question3 = input("Write ? :")

    if question3 == "y" or question3 == "Y":
        print(variable_number)
    else:
        exit(0)

def bool_variable(variable_boolean):
    question4 = input("Write ? :")

    if question4 == "y" or question4 == "Y":
        print(variable_boolean)
    else:
        exit(0)