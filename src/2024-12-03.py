import re

"""
    1. read file
    2. get every instance of mul(number[1-3], number[1-3]) - try regex
    3. parse every number, multiply & compute
    * 
    4. easiest way - replace do with mul(1,0) + dont with mul(0,1)
"""
ENABLE_DIR = "do()"
DISABLE_DIR = "don't()"
enabled = True


def read_file(filename) -> list:
    f = open(filename, "r")
    return f.readlines()


lines = read_file("resources\\2024-12-03.txt")

mul_valid = []


def parse_line(line: str):
    # it was the fastest way to implement the additional logic. it's obviously hack ;)
    # instead we should use "stack" or split by EN&DIS directives
    line = line.replace(ENABLE_DIR, "mul(1,0)")
    line = line.replace(DISABLE_DIR, "mul(0,1)")
    return re.findall("mul\((?P<first>\d{1,3}),(?P<second>\d{1,3})\)", line)


for line in lines:
    mul_valid += parse_line(line)


valid_sum = 0
for mul in mul_valid:
    if mul == ("1", "0"):
        enabled = True
        continue

    if mul == ("0", "1"):
        enabled = False
        continue

    if enabled:
        valid_sum += int(mul[0]) * int(mul[1])


print(f"Sum of valid multiplication is {valid_sum}")
