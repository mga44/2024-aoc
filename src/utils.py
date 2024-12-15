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
