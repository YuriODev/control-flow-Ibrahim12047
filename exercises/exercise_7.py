# Your solution to Exercise 7
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, /, *, mod, pow, div): ")

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '/':
    if num2 == 0:
        result = "Division by 0!"
    else:
        result = num1 / num2
elif operation == '*':
    result = num1 * num2
elif operation == 'mod':
    result = num1 % num2
elif operation == 'pow':
    result = num1 ** num2
elif operation == 'div':
    if num2 == 0:
        result = "Division by 0!"
    else:
        result = num1 // num2
else:
    result = "Invalid operation"

print(f'Result: {result}')
