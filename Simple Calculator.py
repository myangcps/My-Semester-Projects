#Simple Calculator

#Initialize
#Functions
#Adds two numbers together and prints the result
def add(num1, num2):
    result=num1+num2
    print(result)

#Subtracts two numbers together
def subtract(num1, num2):
    result=num1-num2
    print(result)

#Multiply two numbers together
def multiply(num1, num2):
    result=num1*num2
    print(result)

#Divides two numbers together
def divide(num1, num2):
    result=num1/num2
    print(result)

#Main
#Welcomes user to the program
print("Welcome to Simple Calculator")
#Gives the user different options, add, subtract, multiply, divide, or quit the calculator.
while True:
    print("Please select an operation: " )
    print("""
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Quit""")
    operation = int(input("(1-5) Option: "))
    if operation == 1:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        add(num1, num2)
    elif operation == 2:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        subtract(num1, num2)
    elif operation == 3:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        multiply(num1, num2)
    elif operation == 4:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        divide(num1, num2)
    elif operation == 5:
        print("Thank you for using Simple Calculator")
        break
