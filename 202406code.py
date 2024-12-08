from collections import defaultdict
import copy
import time

start_time = time.time()

with open("202406input.txt") as file: D = file.read().split('\n')

AOC_ANS = (5531, 2165)

nrows, ncols = len(D), len(D[0])

obst = set() # default dict not needed 
visited = set()

# register the obstacles in a dictionary and find the start position of the guard. 
for row, line in enumerate(D):
    for col, char in enumerate(line):
        if char == '#':
            obst.add((row,col))
        elif char != '.':
            s_pos = (row,col)
            s_dir = '^>v<'.find(char)

#         ^       >       v     <
DIRS = [(-1,0), (0,1), (1,0), (0,-1)]

p1 = p2 = 0

# Guard moves until they leave the grid or turn right as they hit an obstacle
def guard_movements(start_pos, start_dir, l_obst):
    looped = False
    visited = set()
    pos, cur_dir = start_pos, start_dir
    while 0 <= pos[0] < nrows and 0 <= pos[1] < ncols:
        if (pos, cur_dir) in visited:
            looped = True
            break
        visited.add((pos, cur_dir))
        new_pos = (pos[0]+DIRS[cur_dir][0], pos[1]+ DIRS[cur_dir][1])
        if new_pos in l_obst:
            cur_dir = (cur_dir+1)%4
        else: 
            pos = new_pos
    return looped, visited 

# for P1 we need to find the length of visited, and we need visited for P2
_, visited = guard_movements(s_pos, s_dir, obst)
locations = set((x,y) for (x,y), _ in visited)
print(f"p1: {len(locations)}")

p1_time = time.time()
print(f"Execution Time P1: {p1_time - start_time:6f} seconds")

# for P2 we place a new obstacle in every location visited, but the start pos. 
for location in locations:
    if location == s_pos:
        continue
    new_obst = obst.copy()
    new_obst.add(location)
    left_grid, visited = guard_movements(s_pos, s_dir, new_obst)
    p2 += left_grid

print(f"p2: {p2}")

p2_time = time.time()

print(f"P2 execution Time: {p2_time - p1_time:6f} seconds")
print(f"Total execution Time: {time.time() - start_time:6f} seconds")



