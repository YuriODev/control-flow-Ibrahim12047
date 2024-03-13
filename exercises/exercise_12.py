# Your solution to Exercise 12
number = int(input("Enter a four-digit number: "))
even_replaced = ''.join('*' if int(digit) % 2 == 0 else digit for digit in str(number))
print(even_replaced)
