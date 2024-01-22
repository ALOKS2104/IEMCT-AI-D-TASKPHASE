def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def modulus(x, y):
    return x % y
def exponent(x, y):
    return x ** y
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /, %, **): ")
if operation == '+':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif operation == '-':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif operation == '*':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif operation == '/':
    print(f"{num1} / {num2} = {divide(num1, num2)}")
elif operation == '%':
    print(f"{num1} % {num2} = {modulus(num1, num2)}")
elif operation == '**':
    print(f"{num1} ** {num2} = {exponent(num1, num2)}")
else: print("Invalid operation selected")