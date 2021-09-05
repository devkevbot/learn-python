countries = ["Argentina", "Canada", "Brazil", "United States", "El Salvador"]
print(f"Initial countries: {countries}")
countries.sort()
print(f"Alphabetically sorted countries: {countries}")

print()
numbers = [10, 3, 400, 16, 8, 3012]
print(f"Initial numbers: {numbers}")
numbers.sort()
print(f"Ascending sorted numbers: {numbers}")
numbers.sort(reverse=True)
print(f"Descending sorted numbers: {numbers}")

print()
fruits = ["BANANA", "apPle", "ORange", "mango"]
print(f"Initial fruits: {fruits}")
fruits.sort(key=str.lower)
print(f"Sorted fruits based on lowercase representation: {fruits}")

print()
letters = ["a", "b", "c"]
print(f"Initial letters: {letters}")
letters.reverse()
print(f"Reversed letters: {letters}")
