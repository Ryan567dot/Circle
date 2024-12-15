import math

def calculate(radius=1.0):
    area = math.pi * radius**2
    circumference = 2 * math.pi * radius
    return area, circumference

default_area, default_circumference = calculate()
print(f""&quot;Default Area: {default_area}&quot;)
print(f""&quot;Default Circumference: {default_circumference}&quot;)