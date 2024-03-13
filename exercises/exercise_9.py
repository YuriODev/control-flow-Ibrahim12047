# Your solution to Exercise 9
number = int(input("Enter a three-digit number: "))
first_digit = number // 100
last_digit = number % 10
middle_digit = (number // 10) % 10
sum_first_last = first_digit + last_digit
if sum_first_last > middle_digit:
    result = ">"
elif sum_first_last < middle_digit:
    result = "<"
else:
    result = "="
print(result)



