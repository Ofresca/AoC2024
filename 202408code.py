from collections import defaultdict
from itertools import combinations
import time

start_time = time.time()

ANS = [261, 898]

with  open("202408input.txt") as file: D = file.read().split('\n')

antinodes_p1, antinodes_p2 = set(), set()
antennas = defaultdict(list)

nrows, ncols = len(D), len(D[0])

for row, line in enumerate(D):
    for column, char in enumerate(line):
        if char != '.':
            antennas[char].append((row,column))

# An antinode occurs at any point that is perfectly in line with two antennas of the same frequency - but only when one of the antennas is twice as far away as the other

# twice as far away 

def twice_as_far(pos1, pos2):
    row1, col1 = pos1
    row2, col2 = pos2
    apos1 = (row1 + 2 * (row2 - row1), col1 + 2 * (col2 - col1))
    apos2 = (row2 + 2 * (row1 - row2), col2 + 2 * (col1 - col2))
    return apos1, apos2 
    
def add_antinodes_p1(locations, t_antinodes):
    for pos1, pos2 in combinations(locations, 2):
        new_antinodes = twice_as_far(pos1, pos2)
        for new_antinode in new_antinodes:
            if new_antinode[0] in range(nrows) and new_antinode[1] in range(ncols)and new_antinode not in t_antinodes:
                t_antinodes.add(new_antinode)
    return t_antinodes

def add_antinodes_p2(locations, t_antinodes):
    for pos1, pos2 in combinations(locations, 2):
        new_antinodes = twice_as_far(pos1, pos2)
        t_antinodes.update([pos1, pos2])
        for new_antinode in new_antinodes:
            if new_antinode[0] in range(nrows) and new_antinode[1] in range(ncols)and new_antinode not in t_antinodes:
                t_antinodes.add(new_antinode)
                add_antinodes_p2([new_antinode, pos1], t_antinodes)
                add_antinodes_p2([new_antinode, pos2], t_antinodes)
    return t_antinodes

for antennatype in antennas:
    t_antinodes = set()
    antinodes_p1.update(add_antinodes_p1(antennas[antennatype], t_antinodes))

for antennatype in antennas:
    t_antinodes = set()
    antinodes_p2.update(add_antinodes_p2(antennas[antennatype], t_antinodes))

# print(antinodes)
# visualize_grid(antennas, antinodes, nrows, ncols)
print(f"P1: {len(antinodes_p1)}")
print(f"P2: {len(antinodes_p2)}")

print(f"Execution Time: {time.time() - start_time:6f} seconds")
    


