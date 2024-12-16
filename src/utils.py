def read_lines(filename:str) -> list:
    f = open(filename, "r")
    return f.readlines()

def read_2d_array(filename:str) -> list:
    return [list(s.replace("\n", "")) for s in read_lines(filename)]



def get_2d_array_size(arr):
    max_y = len(arr) - 1
    max_x = len(arr[0]) - 1
    return max_x, max_y

def print_2d_array(arr):
    print("\n".join("".join(i) for i in arr))

def find_char_in_2d_array(arr, character, single=True) -> tuple|list:
    result_list = []
    for i, line in enumerate(arr):
        for j, char in enumerate(line):
            if char == character:
                if single:
                    return (j, i)
                else:
                    result_list.append((j,i))
                    
    return result_list