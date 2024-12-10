import time
from collections import defaultdict

ANS = [794, 1706]

start_time = time.time()

with open("202410input.txt") as file: D = file.read().split('\n')

# Create a dictionary where each height gives a list of their location(s). 
height_locs = defaultdict(list)
for row, line in enumerate(D):
    for col, char in enumerate(line):
        if char != ".":
            height_locs[int(char)].append((row,col))

# Directions for movement (up, right, down, left)
DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

p1, p2 = 0, 0 

#Function to find all possible next steps from the current positions at a given height.
def next_steps(opts, height, height_dict):
    # Next search will be for next height
    height += 1
    # Create a new list of positions reached
    next_opts = []
    # For each line check in all directions if the last position can reach a position higher. 
    for idx, path in enumerate(opts):
        (r,c) = path[-1] # Last location of current path
        for (d_r, d_c) in DIRS:
            n_r, n_c = r+d_r, c+d_c
            if (n_r, n_c) in height_dict[height]:
                next_opts.append(opts[idx] + [(n_r,n_c)])             
    return next_opts, height

# Initialization: Use all 0 in the graph
for r,c in height_locs[0]:
    cur_height = 0
    # For P2 path should be a list of locations visited.
    # [[(r,c),(r,c)...(r,c)], [(r,c),(r,c)...(r,c)], etc. 
    path = [[(r,c)]] # Start with the 0 location used. 
    
    # Loop until height = 9.
    while cur_height < 9:
        path, cur_height = next_steps(path, cur_height, height_locs)

    # For P1 add each unique 9 location visited
    p1 += len(set(line[-1] for line in path))
    # For P2 add all unique paths to each location
    p2 += len(path)

print(f"P1: {p1}")
print(f"P2: {p2}")

p2_time = time.time()
print(f"Total time = {p2_time - start_time:6f} s")

