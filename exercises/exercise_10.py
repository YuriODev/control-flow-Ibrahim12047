# Your solution to Exercise 10
x1, y1 = map(int, input("Enter coordinates of vertex 1 (x, y): ").split())
x2, y2 = map(int, input("Enter coordinates of vertex 2 (x, y): ").split())
x3, y3 = map(int, input("Enter coordinates of vertex 3 (x, y): ").split())
a = (x1 - x2) ** 2 + (y1 - y2) ** 2
b = (x2 - x3) ** 2 + (y2 - y3) ** 2
c = (x3 - x1) ** 2 + (y3 - y1) ** 2
if a + b == c or a + c == b or b + c == a:
    print("Yes, the triangle is right-angled.")
else:
    print("No, the triangle is not right-angled.")
