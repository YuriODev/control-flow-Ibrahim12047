# Your solution to Exercise 14
number = input("Enter a four-digit number: ")
if number[0] == number[3] and number[1] == number[2]:
    is_palindrome = True
else:
    is_palindrome = False
print(is_palindrome)
