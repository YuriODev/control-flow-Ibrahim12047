# Your solution to Exercise 6
x1 = int(input("Enter x-coordinate of point A: "))
y1 = int(input("Enter y-coordinate of point A: "))
x2 = int(input("Enter x-coordinate of point B: "))
y2 = int(input("Enter y-coordinate of point B: "))

dA = x1**2 + y1**2
dB = x2**2 + y2**2

if dA > dB:
    print("Point A is further from the origin.")
elif dB > dA:
    print("Point B is further from the origin.")
else:
    print("The distances from the origin are the same.")