"""
Return the nth Fibonacci number.
n = 1 is F0
n = 2 is F1
and so forth...
"""


def getNthFib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1

    return getNthFib(n - 1) + getNthFib(n - 2)
