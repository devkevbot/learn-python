"""
Decorator: a function that takes another function and extends its behaviour without modifying it.
"""

import functools


def say_hello(name):
    return f"Hello, {name}."


def greet(greeting_func):
    """
    Functions are first-class objects.
    As such, they can be passed in as function arguments.
    """
    return greeting_func("Kevin")


print(greet(say_hello))


def parent(num):
    """
    Functions inside other functions.
    """
    def first_child():
        return "Hi, I'm the first child"

    def second_child():
        return "Hello, I'm the second child"

    if num == 1:
        return first_child
    else:
        return second_child


first = parent(1)
second = parent(2)
print()
print(first())
print(second())

# Simple decorator


def my_decorator(func):
    def wrapper():
        print("Before...")
        func()
        print("After...")
    return wrapper


def say_whee():
    print("Whee!")


say_whee = my_decorator(say_whee)
print()
say_whee()

# Decorator syntax


def do_twice(func):
    @functools.wrap(func)  # Ensure the name of func is bound
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice


@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi, {name}"


print()
message = return_greeting("Kevin")
print(message)
