import time  
from collections import defaultdict
from functools import cache

# ANS = [280, 606411968721181]

start_time = time.time()

with open("202419input.txt") as file: D = file.read().strip().split('\n\n')

# Only P1

# Possible patterns set up 
patterns = defaultdict(set)
# Sort by first letter
for pattern in D[0].split(', '):
    patterns[pattern[0]].add(pattern)

designs = D[1].split('\n') # Requested patterns

# P1 Calculations
p1 = 0
for design in designs:
    # For each design, start with the full design
    Q = set([design])
    while Q:
        design = Q.pop()
        # If the design is in patterns, it is a valid design.
        if design in patterns[design[0]]:
            p1 += 1
            break
        else: 
            # Check to which patterns the design can be matched. 
            # Use first letter for speed purposes.
            for pattern in patterns[design[0]]:
                if design[:len(pattern)] == pattern:
                    # If we can remove a pattern, remove and add to Q
                    Q.add(design.removeprefix(pattern))

print(f"P1 = {p1}")
p1_time = time.time()
print(f"P1 time = {p1_time - start_time:6f}")

# P1 and P2 together
p2, p1 = 0, 0

# P2 calculation with memoization
@cache
def check_patterns(design: str) -> int:
    # If design is empty it is a valid combination
    if design == '':
        return 1
    total = 0 
    # Try every pattern that could match the start of the current design
    for pattern in patterns[design[0]]:
        if design[:len(pattern)] == pattern:
            # Recursively check the remainder
            total += check_patterns(design.removeprefix(pattern)) 
    return total

# P1 and P2 count
results = list(map(check_patterns, designs))
p1 = sum(map(bool, results))
p2 = sum(results)

print(f"P1 = {p1}")
print(f"P2 = {p2}")
p2_time = time.time()
print(f"P2 time = {p2_time - p1_time:6f}")
print(f"Total time = {p2_time - start_time:6f}")

