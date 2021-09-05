def foo():
    print("foo was called!")


def add2(a, b):
    return a + b


def greet(name="Kevin"):
    print(f"Hello, {name}")


def arbitrary_num_arguments(*args):
    print(f"Got {len(args)} args.")
    for arg in args:
        print(arg)


def keyword_args(first, second):
    print(f"First: {first}, Second: {second}")


def arbitrary_keyword_args(**kwargs):
    print(f"Got {len(kwargs)} kwargs.")

    first_name = kwargs["fname"]
    print(f"First name is: {first_name}")

    last_name = kwargs["lname"]
    print(f"Last name is: {last_name}")


foo()

print(add2(2, 4))

# Default arguments
greet()
greet("Charles")

arbitrary_num_arguments(1, 2, 3, 4)

# Keyword arguments
keyword_args(1, 2)
keyword_args(first=2, second=1)

arbitrary_keyword_args(fname="Tom", lname="Scott")
