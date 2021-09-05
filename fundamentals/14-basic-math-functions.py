import math

lowest_number: int = min(1, 30, 8000)
highest_number: int = max(1, 30, 8000)

print(f"Low of: {lowest_number}, High of: {highest_number}")

abs_val: float = abs(-300123123.44)
print(f"Absolute value of -300123123.44 is: {abs_val}")

two_to_the_six: int = pow(2, 6)
print(f"2^6 is: {two_to_the_six}")

# Math module functions
root: float = math.sqrt(125)
print(f"Square root of 125 is: {root}")

ceil_val: int = math.ceil(3.3)
floor_val: int = math.floor(3.3)
print(f"Ceiling of 3.3 is: {ceil_val}, Floor of 3.3 is: {floor_val}")


def area_of_circle(radius: float) -> float:
    return math.pi * math.pow(radius, 2)


print(f"Area of circle with radius 5 is: {area_of_circle(5)}")

print(f"Natural log of e is: {math.log(math.e)}")

print(f"Sin of pi/2 is: {math.sin(math.pi/2)}")

print(f"3 choose 2 is: {math.comb(3,2)}")
