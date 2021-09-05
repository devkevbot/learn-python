# Arithmetic operators
sum_int = 3 + 5
difference_float = 9.9 - 0.1
product_int = 2 * 24
quotient_int = 10 / 4
floor_quotient = 10 // 4
modulus = 27 % 20
exponentiation = 2**6

print(f"3 + 5 is: {sum_int}")
print(f"9.9 - 0.1 is: {difference_float}")
print(f"2 * 24 is: {product_int}")
print(f"10 / 4 is: {quotient_int}")
print(f"10 // 4 is: {floor_quotient}")
print(f"27 % 20 is: {modulus}")
print(f"2 to the power of 6 is: {exponentiation}")

# Arithmetic assignment operators
print()
init_val = 0
init_val += 1
init_val -= 2
init_val *= 3
init_val /= 2
init_val %= 6
init_val //= 1
init_val **= 4
print(init_val)

# Bitwise assingment operators
bit_init = 0  # 0 is b000
bit_init |= 7  # OR, 7 is b111
bit_init &= 5  # AND, 5 is b101
bit_init ^= 5  # XOR
bit_init ^= 5
bit_init >>= 1  # Shift right by 1
bit_init <<= 2  # Shift left by 2
print(bin(bit_init))

# Comparison operators
print()
print(5 == 5)
print(5 != 6)
print(5 > 6)
print(5 < 6)
print(5 >= 5)
print(5 <= 6)

# Logical operators
print()
print(5 == 5 and 4 == 4)
print(5 == 5 or 3 < 2)
print(not(5 == 5))

# Identity operators
print()
first_int = 1
second_int = 1
print(first_int is second_int)  # True

first_list = [1, 2, 3]
second_list = [1, 2, 3]
print(first_list is second_list)  # False

# Membership operators
print()
print(3 in [1, 2, 3])
print(4 not in [6, 7, 8])

# Bitwise operators
print()
print(bin(1 & 1))
print(bin(1 | 0))
print(bin(5 ^ 5))
print(bin(~5))
print(bin(5 << 2))
print(bin(5 >> 1))
