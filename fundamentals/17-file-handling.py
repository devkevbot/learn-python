def read_whole_file(path_to_file):
    f = open(path_to_file)
    print(f.read())
    f.close()


def read_single_line(path_to_file):
    f = open(path_to_file)
    print(f.readline())
    f.close()


def loop_through_file_lines(path_to_file):
    f = open(path_to_file)
    for index, line in enumerate(f):
        print(f"Lenth of line {index} is {len(line)}")
    f.close()


file_name = "sample_input.txt"

read_whole_file(file_name)

print()
read_single_line(file_name)

print()
loop_through_file_lines(file_name)
