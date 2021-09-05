fruits = ["Apple", "Banana", "Mango"]


def print_fruits():
    print(f"List is now: {fruits}")


print_fruits()
print(f"First item in the list is: {fruits[0]}")
print(f"Last item in the list is: {fruits[-1]}")
print(f"The list is {len(fruits)} elements long")
print(f"The second and third items in the list are {fruits[1:3]}")

# Insert at a given index
print()
print("Inserting a pear before the banana!")
fruits.insert(1, "Pear")
print_fruits()

# Append
print()
print("Appending a watermelon!")
fruits.append("Watermelon")
print_fruits()

# Concatenate two lists
print()
print("Concatenating with a new fruit list...")
new_fruits = ["Grape", "Orange", "Tangerine"]
fruits.extend(new_fruits)
print_fruits()

# Remove specific element by string
print()
print("Removing the banana!")
fruits.remove("Banana")
print_fruits()

# Pop
print()
print("Popping the last element!")
fruits.pop()
print_fruits()

# Remove via specific index
print()
print("Removing fruit at the index=3 !")
del fruits[3]
print_fruits()
