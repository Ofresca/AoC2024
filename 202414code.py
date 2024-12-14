import time 
from collections import defaultdict

ANS = [225648864, 7847]

start_time = time.time()

with open("202414input.txt") as file: D = file.read().split('\n')

# 101 tiles wide and 103 tiles tall
n_c = 101 # wide
n_r = 103 # tall

# read data into default dict
# x = col, y = row
robots = defaultdict(list)
for line in D:
    p, v = line.split()
    c_p, r_p = map(int, p.split('=')[1].split(',')) # note col, row
    c_v, r_v = map(int, v.split('=')[1].split(',')) # note col, row
    robots[(r_p, c_p)].append((r_v, c_v))

# When a robot would run into an edge of the space they're in, they instead teleport to the other side
# Where will the robots be after 100 seconds?
# To determine the safest area, count the number of robots in each quadrant after 100 seconds
# Robots that are exactly in the middle (horizontally or vertically) don't count as being in any quadrant, so the only relevant robots are:
# 1, 3, 4, and 1 robot, safety factor of 12

p1 = p2 = 0

# p = position, v = velocity 
# p=0,4 v=3,-3 

def move(robots, steps):
    n_robots = defaultdict(list)
    for (r_p, c_p), vels in robots.items():
        for (r_v, c_v) in vels: 
            nr_p = (r_p + steps*r_v) % n_r
            nc_p = (c_p + steps*c_v) % n_c
            n_robots[(nr_p, nc_p)].append((r_v, c_v))
    return n_robots

def visualize_grid(robots, ncols, nrows):
    print('='*ncols)
    # Create a grid where empty positions are filled with '.'
    grid = [['.' for _ in range(ncols)] for _ in range(nrows)]
    # Mark specified positions with '#'
    for pos, vels in robots.items():
        r, c = pos
        grid[r][c] = str(len(vels))
    print('\n'.join(''.join(row) for row in grid))
    print('='*ncols)

m_r = n_r // 2
m_c = n_c // 2

def safety_score(robots):
    q1, q2, q3, q4 = 0,0,0,0
    for pos, vels in robots.items():
        r, c = pos
        if r < m_r and c < m_c:
            q1 += len(vels)
        elif r < m_r and c > m_c:
            q3 += len(vels)
        elif r > m_r and c < m_c:
            q2 += len(vels)
        elif r > m_r and c > m_c:
            q4 += len(vels)
    return q1 * q2 * q3 * q4

# P1, 100 steps
p1 = safety_score(move(robots, 100))

print(f"P1 = {p1}")
p1_time = time.time()
print(f"P1 time = {p1_time - start_time:6f}")

# find the Christmas tree in the image 
idx = 0 
c_min = 125*125*125*125
idx_min = 0
n_robots = robots.copy()
while True:
    idx += 1
    n_robots = move(n_robots,1)
    n_min = safety_score(n_robots)
    if n_min < c_min:
        c_min = n_min
        idx_min = idx
    if idx > idx_min + 5000:
        # If we did not improve the safety score for 5000 iterations
        break
    if idx == 100000:
        break

print(f"P2 = {idx_min}") 
visualize_grid(move(robots,idx_min), n_c, n_r)

p2_time = time.time()
print(f"P2 time = {p2_time - p1_time:6f}")
print(f"Total time = {p2_time - start_time:6f}")
