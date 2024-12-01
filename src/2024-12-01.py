"""
    1. parse file into first[] & second[]
    2. sort lists
    3. calculate distances into sep. list (can be variable instead)
    * 
    4. iterare over first
    5. for each entry find how many times it accurs in second
    6. calculate & add to similaroty score num * count
"""


def read_file(filename):
    f = open(filename, "r")
    first, second = [], []
    for l in f.readlines():
        l = l.split()
        first.append(int(l[0]))
        second.append(int(l[1]))

    return first, second


first, second = read_file("resources\\2024-12-01.txt")

first = sorted(first)
second = sorted(second)

totalDistance = 0
for i in range(len(first)):
    totalDistance += abs(first[i] - second[i])

print(f"total distance is {totalDistance}")

similarityScore = 0
for num in first:
    # perf: instead of calling count every time, we can create dict {number: number_of_occurs}
    count = second.count(num)
    similarityScore += num * count 
    
print(f"similarity score is {similarityScore}")
