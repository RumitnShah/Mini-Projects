def addition(n1, n2):  # Define a function for addition
    sum = n1 + n2
    return sum

def subtraction(n1, n2):  # Define a function for subtraction
    sub = n1 - n2
    return sub

def multiplication(n1, n2):  # Define a function for multiplication
    multiply = n1 * n2
    return multiply

def division(n1, n2):  # Define a function for division
    divide = n1/n2
    return divide

operation = 0  # Initialize variable for operation choice

# Start a loop until the user chooses to end the program
while operation != 5:
    # Print menu for the user to choose an arithmetic operation
    print("""\nChoose any Arithmetic Operation you want to perform:
    (1)Addition
    (2) Subtraction
    (3) Multiplication
    (4) Division
    (5) END --- To close the calculator""")

    # Ask user to enter operation choice
    operation = int(input("Enter the operation number: "))

    # Ask user to enter two numbers
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))

    # Perform the chosen operation based on user input
    if operation == 1:
        print("\nThe Addition of numbers is ", addition(n1, n2))

    elif operation == 2:
        print("\nThe Subtraction of numbers is ", subtraction(n1, n2))

    elif operation == 3:
        print("\nThe Multiplication of numbers is ", multiplication(n1, n2))

    elif operation == 4:
        print("\nThe Division of numbers is ", division(n1, n2))

    elif operation == 5:
        break  # Exit the loop if user chooses to end the program

    else:
        print("\nEnter proper operation number!")   # Error message for invalid operation choice

