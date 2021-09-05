def example_1():
    """
    Shows the basic try/except structure.
    """
    try:
        print(undefined)  # Won't work because this variable has not been set.
    except:
        print("An exception occurred.")


def example_2():
    """
    Shows how specific error types can be caught by using the form except <T>.
    """
    try:
        print(undefined)
    except NameError:
        print("Variable is undefined.")
    except:
        print("An exception occurred")


def example_3():
    """
    Shows how else blocks are run if no exception is thrown.
    """
    try:
        print("Cats are cool")
    except:
        print("Something went wrong...")
    else:
        print("Nothing went wrong.")


def example_4():
    """
    Shows the use of the finally block, which is always executed.
    """
    try:
        print(undefined)
    except:
        print("Something went wrong...")
    finally:
        print("This is printed regradless.")


def example_5():
    """
    Shows how to raise an exception.
    """
    var: str = "Hello"
    if not type(var) is int:
        raise TypeError("Expected an integer")


example_1()

print()
example_2()

print()
example_3()

print()
example_4()

print()
example_5()
