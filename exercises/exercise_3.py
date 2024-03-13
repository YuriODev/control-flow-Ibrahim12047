# Your solution to Exercise 3
a = ''
def checkrcolor(number):
    if number < 0 or number > 36:
        a = "The bet will not play. Please enter a number between 0 and 36."
    if number == 0:
        a = "Green"
    if (number >= 1 and number <= 10) or (number >= 19 and number <= 28):
        a = "Red" if number % 2 == 1 else "Black"
    if (number >= 11 and number <= 18) or (number >= 29 and number <= 36):
        a = "Black" if number % 2 == 1 else "Red"
number = int(input("Enter a number from 0 to 36: "))
print(a)
