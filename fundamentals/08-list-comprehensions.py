numbers = [0, 1, 2, 3, 4]
print(f"Starting numbers: {numbers}")

squared_numbers = [num*num for num in numbers]
print(f"Squared numbers: {squared_numbers}")

even_numbers_between_0_and_10 = [num for num in range(0, 11) if num % 2 == 0]
print(f"Even numbers between 0 and 10: {even_numbers_between_0_and_10}")

fruits = ["Apple", "Banana", "Orange"]
print(f"Starting fruits: {fruits}")
fruits_ending_with_e = [
    fruit for fruit in fruits if fruit.endswith("e")
]
print(f"Fruits ending with the letter 'e': {fruits_ending_with_e}")

upper_case_banana_only = [
    fruit.upper()
    for fruit in fruits if fruit == "Banana"
]
print(f"Upper case banana only: {upper_case_banana_only}")

orange_finder = ["NO" if fruit != "Orange" else "YES" for fruit in fruits]
print(orange_finder)
