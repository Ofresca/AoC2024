import time
from collections import defaultdict
from itertools import combinations
from random import shuffle

start_time = time.time()

# ANS = [1238, [bg,bl,ch,fn,fv,gd,jn,kk,lk,pv,rr,tb,vw] (len = 13)]

with open("202423input.txt") as file: D = file.read().strip().split('\n')

p1, p2 = 0, 0

# Dictionary to store connections between computers
connected_to = defaultdict(set)

for line in D: 
    pc1, pc2 = line.split('-')
    connected_to[pc1].add(pc2)
    connected_to[pc2].add(pc1)

# --- Part 1: Count sets of 3 inter-connected pcs containing at least one 't' starting PC --- 
matched = set()
for pc1 in connected_to:
    if pc1.startswith('t'):
        for pc2, pc3 in combinations(connected_to[pc1], 2):
            comb = frozenset([pc1, pc2, pc3])
            if comb not in matched and pc3 in connected_to[pc2]:
                p1 += 1
                matched.add(comb)

print(f"P1 = {p1}")
p1_time = time.time()
print(f"P1 time = {p1_time - start_time:6f}")

# --- Part 2: Find the largest connected component ---

def check_connected(pc_list: set, new_pc: str) -> bool:
    if new_pc not in pc_list:
          if pc_list <= connected_to[new_pc]:
               return 1
          else:
            return 0
    else:
        return 1

def dfs(visited: set, pc_list: set, pc: str) -> set:
    if pc not in visited:
        visited.add(pc) 
        if check_connected(pc_list, pc):
            pc_list.add(pc)
            for new_pc in connected_to[pc]:
                dfs(visited, pc_list, new_pc)

# Generate lists of all interconnected components. 
connected = []
for pc in connected_to: 
    visited = {}
    pc_list = {pc}
    dfs(visited, pc_list, pc)
    connected.append(pc_list)

longest_seq = max(connected, key=len)
p2 = ','.join(sorted(longest_seq))

print(f"P2 = {p2}")
p2_time = time.time()
print(f"P2 time = {p2_time - p1_time:6f}")
print(f"Total time = {p2_time - start_time:6f}")