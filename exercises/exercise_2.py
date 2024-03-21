# Your solution to Exercise 2
a=""
age = int(input("Enter the person's age: "))
if age <= 1:
    a=("The person is an infant.")
elif age < 13:
    a=("The person is a child.")
elif age < 20:
    a=("The person is a teenager.")
else:
    a=("The person is an adult.")