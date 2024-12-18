import time 
from collections import deque

# ANS = [294, [31, 22]]

start_time = time.time()

with open("202418input.txt") as file: D = file.read().strip().split('\n')
D = [list(map(int, x.split(','))) for x in D]

p1, p2 = 0, 0

n_cols = n_rows = 71 # 0 - 70 -> 71 rows and columns 

# Starting and ending positions
s_pos = (0,0) 
e_pos = (n_rows-1, n_cols-1)
bytes = 1024 # 1024 for part 1

# Directions for BFS (up, right, down, left)
DIRS4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(start, blocked):
    steps = 0
    queue = deque([(start, steps)])
    visited = set([start])
    while queue:
        (c_pos), steps = (r,c), _ = queue.popleft()
        if c_pos == e_pos:
            return steps
        for dr,dc in DIRS4:
            n_pos = (nr, nc) = (r+dr, c+dc)
            if nr in range(n_rows) and nc in range(n_cols) and n_pos not in visited and n_pos not in blocked:
                visited.add(n_pos)
                queue.append((n_pos, steps + 1))

# Number of blocked positions for part 1 (1024 positions)
fallen_bytes = {tuple(x) for x in D[:bytes]} # Set

# Do a BFS to find the shortest path. 
p1 = bfs(s_pos, fallen_bytes)

print(f"P1 = {p1}")
p1_time = time.time()
print(f"P1 time = {p1_time - start_time:6f}")

p2 = 0 
i = len(D)
fallen_bytes = {tuple(x) for x in D} # Set

# Find when the last path is possible by reverse unblocking. 
while not p2:
    i -= 1
    fallen_bytes.remove(tuple(D[i])) # Unblock a position
    p2 = bfs(s_pos, fallen_bytes) # Check if we can find a solution

p2 = D[i]

print(f"P2 = {p2}")
p2_time = time.time()
print(f"P2 time = {p2_time - p1_time:6f}")
print(f"Total time = {p2_time - start_time:6f}")