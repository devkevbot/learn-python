# True conditions
should_do_something = True
if should_do_something:
    print("Doing something!")

# False condition
should_do_something = False
if not(should_do_something):
    print("Waiting for something to do.")

# If, else if, and else block
big_number = 300

if big_number > 500:
    print("Bigger than 500.")
elif big_number > 250:
    print("Bigger than 250.")
else:
    print("Small number!")

# Shorthand if else
print("Bigger than 100.") if big_number > 100 else print("Smaller than 100.")

# Compound conditions
is_banana = True
is_yellow = True

if is_banana and is_yellow:
    print("It's a yellow banana!")

is_apple = False
is_red = True
if is_apple or is_red:
    print("It's either an apple or it's red!")
