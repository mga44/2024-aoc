import utils
from collections import defaultdict
"""
    1. get line
    2. map line to disk_map + list of empty spaces (marked as .)
    3. iterate over line -> find last elem that != '.' and != '#'
    4. swap empty with number, mark swapped as #
    *
    5. 
"""

line = utils.read_lines("resources\\2024-12-09.txt")[0]
line = "2333133121414131402"

def map_line(line:str):
    disk_map = []
    file_index = 0
    empty_spaces = []
    empty_space_groups = []
    disk_entries =[]
    for i in range(len(line)):
        elem_value = int(line[i])
        if i % 2 == 0: #real elem
            entry = []
            index = len(disk_map)
            for _ in range(elem_value):
                disk_map.append(file_index)
                entry.append(index)
                index+=1
            disk_entries.insert(0,(elem_value, file_index, entry))
            file_index +=1
        else: # empty space
            empty_space_index = len(disk_map)
            l = []
            for _ in range(elem_value):
                disk_map.append(".")
                l.append(empty_space_index)
                empty_spaces.append(empty_space_index)
                empty_space_index+=1
            empty_space_groups.append(l)
                
                
    return disk_map, empty_spaces, empty_space_groups, disk_entries
            
    

disk_map, empty_spaces, empty_space_groups, disk_entries = map_line(line)


def get_last_elem(disk_map:list, search_from:int):
    possible_last_elem = None
    for i in range(len(disk_map)-1,search_from, -1):
        if disk_map[i] != '.':
            return disk_map[i], i     
    
    return possible_last_elem


part_1 = False
if part_1:
    for space in empty_spaces:
        last_elem = get_last_elem(disk_map, space)
        if not last_elem:
            break
        
        disk_map[space] = last_elem[0]
        disk_map[last_elem[1]] = "."
 
 
def get_elem(size_max):
    elems = list(filter(lambda x: x[0] <=size_max, disk_entries))
    if not elems:
        return 
    
    
    first_elem = elems[0]
    print(f'removing {first_elem}')
    disk_entries.remove(first_elem)
    return first_elem
    
    
part_2 = True
if part_2:
    #space group: [ind_1, ind_2, ...]
    for space_group in empty_space_groups:
        while space_group != []:
            group_len = len(space_group)
            e = get_elem(group_len) 
            if not e: 
                break
            
            #e: (initial_number, file_id, [ind_1, ...])
            for i in range(len(e[2])):
                empty_ind = space_group[i]
                file_ind = e[2][i]
                
                disk_map[empty_ind] = e[1]
                disk_map[file_ind] = "."
            
            print(f'before {space_group}')
            space_group = space_group[len(e[2]):] 
            print(f'after {space_group}')               
        
            

checksum = 0
for i in range(len(disk_map)):
    el = disk_map[i]
    if el == ".":
        continue
    checksum+= int(el)*i
    
print(f"Checksum is {checksum}")