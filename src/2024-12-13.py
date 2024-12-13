import utils
import re
"""
    1. read file
    2. create struct: [{'A': (X,Y), 'B': (..), 'Prize':(..)}]
    3. ...
    
"""

lines = utils.read_lines("resources\\2024-12-13.txt")

machines = []
machine = {}
for line in lines:
    line = line.strip()
    if 'Button A:' in line:
        a = re.findall(r'[XY]\+(\d+)',line)
        machine['A'] = tuple(map(lambda x: int(x), a))
        print(a)
    
    if 'Button B:' in line:
        a = re.findall(r'[XY]\+(\d+)',line)
        machine['B'] = tuple(map(lambda x: int(x), a))
        print(a)
        
    if 'Prize:' in line:
        a = re.findall(r'[XY]=(\d+)',line)
        machine['Prize'] = tuple(map(lambda x: int(x) + 10000000000000, a))
        # machine['Prize'] = tuple(map(lambda x: int(x), a))
        print(a)
    
    if not line:
        machines.append(machine)
        machine = {}


machines.append(machine)

print(machines)        


def compute_for_machine(machine):
    for a_num in range(100):
        for b_num in range(100):
            p_x = a_num * machine['A'][0] +  b_num * machine['B'][0]
            p_y = a_num * machine['A'][1] +  b_num * machine['B'][1]
            
            if p_x == machine['Prize'][0] and p_y == machine['Prize'][1]:
                return a_num *3 + b_num
    return None
                

def compute_part_2(machine):
    m = ((machine['A'][0] * machine["Prize"][1]) - (machine['A'][1] * machine["Prize"][0])) / (machine['A'][0]*machine['B'][1] - machine['A'][1]*machine['B'][0]) 
    n = (machine["Prize"][0] - m*machine["B"][0]) / machine["A"][0] 
    if m > 0 and n > 0 and m.is_integer() and n.is_integer():
        return n*3 + m
    
    return None

tokens_list = []
for machine in machines:
    tokens = compute_part_2(machine)       
    if tokens:
        tokens_list.append(tokens)
        
        
print(f'Sum of tokens to spend is {sum(tokens_list)}') 
