def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row  # Yield will result in a generator object


# csv_gen = csv_reader("some_csv.txt")
# row_count = 0

# for row in csv_gen:
#     row_count += 1

# print(f"Row count is {row_count}")

"""Generator expressions"""
file_name = "input.csv"
csv_gen = (row for row in open(file_name))


def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


# for i in infinite_sequence():
#     print(i, end=" ")

gen = infinite_sequence()
print(next(gen))  # 0
print(next(gen))  # 1
