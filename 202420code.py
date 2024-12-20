import time 
from collections import deque

# ANS [1327, 985737]

start_time = time.time()

DIRS4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]

with open("202420input.txt") as file: D = file.read().strip().split('\n')

road = set() # Possible positions
track = [] # Ordered positions
steps_from_start = dict()

# Initiate the grid 
for r, line in enumerate(D): 
    for c, char in enumerate(line):
        match char:
            case '.': road.add((r,c))
            case 'S': s_pos = (r,c)
            case 'E': 
                e_pos = (r,c) 
                road.add((r,c)) # Also add the end point to the road

p1, p2 = 0, 0

# Find the track and the length of the track, using altered bfs
# Also fill the distances from start dictionary
def bfs(start: tuple, road: set): # returns the track
    queue = deque([(start, [start])])
    steps_from_start[start] = 0
    while queue:
        (c_pos), track = (r,c), _ = queue.popleft()

        if c_pos == e_pos:
            return track
        
        for dr, dc in DIRS4:
            n_pos = (r + dr, c + dc)
            if n_pos in road and n_pos not in steps_from_start:
                steps_from_start[n_pos] = steps_from_start[c_pos] + 1
                queue.append((n_pos, track + [n_pos]))

track = bfs(s_pos, road)

# Only if at least 100 ps away. 
for idx, pos_1 in enumerate(track[:-100]):
    for r in range(-20,21):  # Iterate over the range of -20 to 20 for rows
        for c in range(-20+abs(r), 21-abs(r)):
            r1, c1 = pos_1
            pos_2 = (r2, c2) = (r+r1, c+c1)
            if pos_2 in steps_from_start:      
                dif = abs(r1 - r2) + abs(c1 - c2)
                # Part 1 & 2       
                if dif <= 20:
                    # We can remove this part for part 2
                    # pss = pico seconds saved
                    pss = steps_from_start[pos_2] - steps_from_start[pos_1] - dif
                    if pss >= 100:
                        p2 += 1
                        # We can also remove if dist = 2, for p1
                        if dif == 2:
                            p1 += 1

print(f"P1 = {p1}")
print(f"P2 = {p2}")

p2_time = time.time()
print(f"Total time = {p2_time - start_time:6f}")