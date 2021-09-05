# Iterate over a list
names = ["Kevin", "Bob", "Alice"]
for name in names:
    print(f"Name is: {name}")

# Print each symbol in a string
for x in "Hello, world.":
    print(x)

# Break out of a loop
for fruit in ["Apple", "Banana", "Mango"]:
    if fruit == "Mango":
        break
    print(fruit)

# Range here is [0, 10)
for i in range(0, 10):
    print(i)

# Execute code after loop is finished
for animal in ["Dog", "Cat", "Sheep"]:
    print(f"Animal: {animal}")
else:
    print("No more animals to print!")

# Empty for loop
for x in [0, 2, 4]:
    pass

# while loops:
count = 0
while(True):
    count += 1
    if count == 100:
        break
print(f"Count is {count}")
