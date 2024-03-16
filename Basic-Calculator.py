import string

# Get list of all letters (both lowercase and uppercase) using string module
letters = list(string.ascii_letters)  

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

def average(n1, n2):  # Define a function for average
    average = (n1 + n2)/2
    return average

operation = 0  # Initialize variable for operation choice

# Start a loop until the user chooses to end the program
while operation != 5:
    # Print menu for the user to choose an arithmetic operation
    print("""\nChoose any Arithmetic Operation you want to perform:
    (1) Addition
    (2) Subtraction
    (3) Multiplication
    (4) Division
    (5) Average
    (6) END --- To close the calculator""")

    # Ask user to enter operation choice
    operation = input("\nEnter the operation number: ")

    for every_letter in letters:  # Check if the input contains any letters
        if operation == every_letter:
            print("Please input numbers instead of characters")
            break  # Exit the loop if user enters characters

    int_operation = int(operation)  # Convert operation to integer
    if int_operation == 6:
        print("Calculator is OFF")
        break  # Exit the loop if user chooses to end the program

    else:
        # Ask user to enter two numbers
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))

        # Perform the chosen operation based on user input
        if int_operation == 1:
            print("\nThe Addition of numbers is ", addition(n1, n2))

        elif int_operation == 2:
            print("\nThe Subtraction of numbers is ", subtraction(n1, n2))

        elif int_operation == 3:
            print("\nThe Multiplication of numbers is ", multiplication(n1, n2))

        elif int_operation == 4:
            print("\nThe Division of numbers is ", division(n1, n2))

        elif int_operation == 5:
            print("\nThe Average of numbers is ", average(n1, n2))

        else:
            print("\nEnter proper operation number!")   # Error message for invalid operation choice

