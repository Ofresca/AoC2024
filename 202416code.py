import time 
import heapq

# ANS = [123540, 665]

start_time = time.time()

with open("202416input.txt") as file: D = file.read().strip().split('\n')

n_r, n_c = len(D), len(D[0])

#           N,0     E,1     S,2     W,3
DIRS4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
s_dir = 1 # Facing East 
walls = set()
SEEN = dict()
best_poss = set()

for r, line in enumerate(D): 
    for c, char in enumerate(line):
        match char:
            case '#': walls.add((r,c))
            case 'S': s_pos = (r,c)
            case 'E': e_pos = (r,c)

p1, p2 = 0, 0

def dijkstras(start, end, s_dir):
    Q = [(0, (start, s_dir, [(start)]))]  # Priority queue
    SEEN[(start, s_dir)] = 0
    min_cost = 1_000_000_000
    while Q:
        (cost, (pos, d, cpath)) = heapq.heappop(Q)
        if pos == end:
            for (pos) in cpath:
                best_poss.add(pos)
            min_cost = min(min_cost, cost)
            continue 
        # Only turn 90 degrees or go straight. 
        for c_d in [d, (d+1)%4, (d-1)%4]:
            # If direction does not change a move costs +1
            # And we move in direction d
            if c_d == d:
                n_cost = cost + 1
                n_pos = (pos[0] + DIRS4[d][0], pos[1] + DIRS4[d][1])
                if n_pos in walls:
                    continue
            # If direction changes, this costs +1000
            # And we do not move
            else:
                n_cost = cost + 1000
                n_pos = pos
            # If move is new or = or cheaper, we make the move. 
            if n_cost <= SEEN.get((n_pos, c_d),min_cost):
                SEEN[(n_pos, c_d)] = n_cost
                heapq.heappush(Q, (n_cost, (n_pos, c_d, cpath+[(n_pos)])))
    return min_cost, len(best_poss)

p1, p2 = dijkstras(s_pos, e_pos, s_dir)

print(f"P1 = {p1}")
print(f"P2 = {p2}")

p2_time = time.time()
print(f"Total time = {p2_time - start_time:6f} s")

