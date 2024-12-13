import utils

"""
    1. list regions
    2. for each region iterate over each elem and check adjacent fields -> add to sum
    3. compute borders * number of elems
""" 

grid = utils.read_2d_array("resources\\2024-12-12.txt")
max_x,max_y = utils.get_2d_array_size(grid)


grid_mask = list(list(0 for _ in range(max_x)) for _ in range(max_y))

print(grid_mask)


def processed(index):
    pass

def process(index, plant):
    if processed(index):
        return 
    
    
    
    process((index[0]-1, index[1]), plant)
    process((index[0]+1, index[1]), plant)
    process((index[0], index[1]-1), plant)
    process((index[0], index[1]+1), plant)
    
    pass

for i in range(max_y):
    for j in range(max_x):
        plant = grid[i][j]
        index = (j, i)
            
        
        
        
        
        