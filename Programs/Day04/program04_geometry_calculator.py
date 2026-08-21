def line():
    print("-" * 34)

# Program 4 — Geometry Calculator
PI = 3.14159


def rectangle_area(length, width):
    return length * width


def circle_area(radius):
    return PI * radius**2


def triangle_area(base, height):
    return 0.5 * base * height


line()
print("Program 4 — Geometry Calculator")
line()
print("Rectangle Area:", rectangle_area(5, 3))
print("Circle Area:", circle_area(5))
print("Triangle Area:", triangle_area(5, 3))