def read_2d_array(filename:str) -> list:
    f = open(filename, "r")
    return [list(s.replace("\n", "")) for s in f.readlines()]



def get_2d_array_size(arr):
    max_y = len(arr) - 1
    max_x = len(arr[0]) - 1
    return max_x, max_y