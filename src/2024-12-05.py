from collections import defaultdict

"""
    1. read input
    2. write rules to a dict, in form of {num : [preceeded_by]}
        rules are in X|Y format -> if we encounter Y in code we must not have X later on
    3. iterate over reports. for each report, check rules to check if next numbers don't violate rules 
    4. if VALID -> get the middle number
    5. if INVALID -> continue 
    *
    6. for invalid reports fix in following way
    7. iterate over each elem. in array. construct new_report and iterate over it to determine max_index where eem should be added
    
"""


def read_file(filename):
    f = open(filename, "r")

    ruleset = defaultdict(list)  # {num : [must_not_be_after]}
    reports = []
    for line in f.readlines():
        if "|" in line:
            x_y = line.split("|")
            ruleset[int(x_y[1])].append(int(x_y[0]))
            continue

        if "," in line:
            reports.append([int(i) for i in line.split(",")])

    return ruleset, reports


ruleset, reports = read_file("resources\\2024-12-05.txt")


def valid_report(report: list):
    for i in range(len(report)):
        elem = report[i]
        for j in range(i + 1, len(report)):
            next_elem = report[j]
            if next_elem in ruleset[elem]:
                return False

    return True


def get_middle_elem(report):
    middle_index = int((len(report) - 1) / 2)
    return report[middle_index]


def fix_report(report: list):
    new_report = []
    for elem in report:
        if new_report == []:
            new_report.append(elem)
            continue

        rules = ruleset[elem]
        possible_index = 0
        for i in range(len(new_report)):
            elem_in_new = new_report[i]
            if elem_in_new in rules:  # elem has to be added after
                possible_index = i + 1

        new_report.insert(possible_index, elem)
        
    return new_report


valid_middle_elems_sum = 0
invalid_middle_elems_sum = 0
for report in reports:
    is_valid = valid_report(report)
    if is_valid:
        valid_middle_elems_sum += get_middle_elem(report)
    else:
        fixed_report = fix_report(report)
        invalid_middle_elems_sum += get_middle_elem(fixed_report)


print(f"Sum of middle elems is {valid_middle_elems_sum}")
print(f"Sum of middle elems after fix is {invalid_middle_elems_sum}")
