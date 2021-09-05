def fibonacci(n: int) -> int:
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(f"Fibonnaci value: {fibonacci(3)}")
print()


def print_star_pattern(n: int) -> None:
    if (n > 0):
        print(n * "*")
        print_star_pattern(n - 1)


print_star_pattern(10)
"""
**********
*********
********
*******
******
*****
****
***
**
*
"""
