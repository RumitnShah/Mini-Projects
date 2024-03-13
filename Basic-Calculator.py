def addition(n1, n2):
    sum = n1 + n2
    return sum

def subtraction(n1, n2):
    sub = n1 - n2
    return sub

def multiplication(n1, n2):
    multiply = n1 * n2
    return multiply

def division(n1, n2):
    divide = n1/n2
    return divide

operation = 0
while operation != 5:
    print("""\nChoose any Arithmetic Operation you want to perform:
    (1)Addition
    (2) Subtraction
    (3) Multiplication
    (4) Division
    (5) END --- To close the calculator""")

    operation = int(input("Enter the operation number: "))

    n1 = int(input("Enter any number: "))
    n2 = int(input("Enter any number: "))

    if operation == 1:
        print("\nThe Addition of numbers is ", addition(n1, n2))

    elif operation == 2:
        print("\nThe Subtraction of numbers is ", subtraction(n1, n2))

    elif operation == 3:
        print("\nThe Multiplication of numbers is ", multiplication(n1, n2))

    elif operation == 4:
        print("\nThe Division of numbers is ", division(n1, n2))

    elif operation == 5:
        break

    else:
        print("\nEnter proper operation number!")

