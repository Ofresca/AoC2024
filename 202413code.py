import time 
from collections import defaultdict
import re
from fractions import Fraction

start_time = time.time()

ANS = [37128, 74914228471331]

with open("202413input.txt") as file: D = file.read().split('\n\n')

p1, p2 = 0, 0
C_A, C_B = 3, 1 # Cost per token

# Parse the input per machine 
machines = defaultdict(list)
# A (x,y), B (x,y), prize (x,y)
for idx, machine in enumerate(D):
    for x,y in re.findall(r'(\d+)\D+(\d+)', machine):
        machines[idx].append((int(x),int(y)))

def min_cost(a_x, a_y, b_x, b_y, p_x, p_y):
    # a_x * a + b_x * b = p_x
    # a_y * a + b_y * b = p_y
    # Solve for a and b
    b = Fraction((a_y * p_x - a_x * p_y), (a_y * b_x - a_x * b_y))
    a = Fraction((p_x - b_x * b), a_x)
    # A solution is only valid if it is an integer
    if b.is_integer() and a.is_integer():
        return C_A * int(a) + C_B * int(b)
    # If no valid solution is found:
    return 0

for machine in machines.values():
    (a_x, a_y), (b_x, b_y), (p_x, p_y) = machine
    p1 += min_cost(a_x, a_y, b_x, b_y, p_x, p_y)

print(f"P1 = {p1}")
p1_time = time.time()
print(f"P1 time = {p1_time - start_time:6f}")

p2_add = 10000000000000
for machine in machines.values():
    (a_x, a_y), (b_x, b_y), (p_x, p_y) = machine
    p2 += min_cost(a_x, a_y, b_x, b_y, p2_add + p_x, p2_add + p_y)

print(f"P2 = {p2}")
p2_time = time.time()
print(f"P2 time = {p2_time - p1_time:6f}")
print(f"Total time = {p2_time - start_time:6f}")
