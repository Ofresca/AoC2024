import time 
from collections import deque, defaultdict

start_time = time.time()

with open("202412input.txt") as file: D = file.read().split('\n')

ANS = [1421958, 885394]

DIRS4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIRSD = [(-1, 1), (1, 1), (1, -1), (-1,-1)]

SEEN = set()

r_plot, c_plot = len(D), len(D[0])
p1, p2 = 0, 0

plot_dict = defaultdict(list)

def garden_plot_sides(pos):
    sides, size = 0, 0
    r,c = pos
    queue = deque([(r,c)])
    visited = set()
    plant = D[r][c]
    while queue:
        (r,c) = queue.popleft()
        if (r,c) in visited:
            continue
        visited.add((r,c))
        size += 1 # for each iteration we have another location
        for dr,dc in DIRS4:
            nr,nc = r+dr, c+dc 
            if not (nr in range(r_plot) and nc in range(c_plot)) or D[nr][nc] != plant:
                sides +=1 
            elif D[nr][nc] == plant:
                queue.append((nr,nc)) # Add new location to queue
    plot_dict[pos] = list(visited)
    SEEN.update(visited)
    return size*sides

for r in range(r_plot):
    for c in range(c_plot):
        pos = (r, c)
        if pos not in SEEN:
            p1 += garden_plot_sides(pos)

print(f"P1 = {p1}")
p1_time = time.time()
print(f"P1 time = {p1_time - start_time}")

for plot in plot_dict.values():
    sides = 0
    for (r,c) in plot:
        for (nr1, nc1), (nr2, nc2) in zip(DIRS4, DIRS4[1:]+[DIRS4[0]]):
            # Outer corners
            sides += ((r+nr1, c+nc1) not in plot and (r+nr2, c+nc2) not in plot)
        for (nr1, nc1), (nr2, nc2), (nrn, ncn) in zip(DIRS4, DIRS4[1:]+[DIRS4[0]], DIRSD):
            # Inner corners
            sides += ((r+nr1, c+nc1)  in plot and (r+nr2, c+nc2) in plot and (r+nrn, c+ncn) not in plot)
    p2 += sides * len(plot) 

print(f"P2 = {p2}")
p2_time = time.time()
print(f"P2 time = {p2_time - p1_time}")
print(f"Total time = {p2_time - start_time}")