"""
    1. read lines 
    2. iterate over each X
    3. for each X, search all directions for M - A - S
    4. inc if found
    *
    5. search for A in lines[1 -- len-1][1 -- len-1]
    6. for each 'A' check corners to locate 'M' 
    7. see if there's corresponding 'S' on the other side (mul vector by -1)
"""


def read_file(filename) -> list:
    f = open(filename, "r")
    return f.readlines()


lines = read_file("resources\\2024-12-04.txt")

every_dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

counter_part_1 = 0
max_x = len(lines[0]) - 1 - 1
max_y = len(lines) - 1


def find_4char_words(initial_index: tuple):
    global counter_part_1
    for dir in every_dir:
        word = "X"
        for i in [1, 2, 3]:
            q = tuple(c * i for c in dir)
            new_index_x = initial_index[0] + q[0]
            new_index_y = initial_index[1] + q[1]
            if (
                new_index_x < 0
                or new_index_y < 0
                or new_index_x > max_x
                or new_index_y > max_y
            ):
                new_char = "."
            else:
                new_char = lines[new_index_y][new_index_x]

            word += new_char
        if word == "XMAS":
            counter_part_1 += 1


counter_part_2 = 0


def find_x_mas(initial_index: tuple):
    x_directions = [(1, 1), (1, -1)]
    is_x_mas = True
    global counter_part_2
    for dir in x_directions:
        first_part = extract_diagonal(initial_index, dir)

        diag = tuple(i * -1 for i in dir)
        second_part = extract_diagonal(initial_index, diag)

        if sorted(first_part + second_part) != ["M", "S"]:
            is_x_mas = False

    if is_x_mas:
        counter_part_2 += 1

def extract_diagonal(initial_index, dir):
    new_index_x = initial_index[0] + dir[0]
    new_index_y = initial_index[1] + dir[1]
    if (
            new_index_x < 0
            or new_index_y < 0
            or new_index_x > max_x
            or new_index_y > max_y
        ):
        first_part = "."
    else:
        first_part = lines[new_index_y][new_index_x]
    return first_part


#perf: complexity O(M*N)
y = 0
for line in lines:
    x = 0
    for char in line:
        index = (x, y)
        if char == "X":
            find_4char_words((x, y))

        if char == "A":
            find_x_mas(index)

        x += 1
    y += 1


print(f"XMAS count: {counter_part_1}")
print(f"X-MAS count: {counter_part_2}")
