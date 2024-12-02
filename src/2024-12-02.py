"""
    1. read file in form of list(list(int))
    2. for each list:
        3. check that tendency is constant => easiest way to compare with sort & reversed sort
        4. check that abs(list(x) - list(x+1)) is between 1 & 3 inclusive
    5. increase counter if conditions are met
    * 
    if either is not met -> iterate over each element, remove it and perform same operations
"""


def read_file(filename):
    f = open(filename, "r")
    lines = []
    for l in f.readlines():
        l = l.split()
        lines.append(list(map(lambda x: int(x), l)))

    return lines


def check_report(report: list):
    incr_sort = sorted(report)
    decr_sort = sorted(report, reverse=True)
    
    if report != incr_sort and report != decr_sort:
        return False
    
    for i in range(len(report)-1):
        num = report[i]
        next = report[i+1]
        difference = abs(num - next)
        if difference < 1 or difference > 3:
            return False
    
    return True  

reports = read_file("resources\\2024-12-02.txt")
counter = 0
for report in reports:
    initial_report_check = check_report(report)
    if initial_report_check:
        counter += 1
        continue
    
    dampened_check = False
    for i in range(len(report)):
        adjusted = report[:i] + report[i+1:]
        dampened_check = check_report(adjusted)
        if dampened_check:
            counter += 1
            break
        
        

print(f"Safe reports: {counter}")