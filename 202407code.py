import itertools
import time 

start_time = time.time()

with open("202407input.txt") as file: D = file.read().split('\n')

# P1: 7710205485870, P2 = 20928985450275 

p1 = p2 = 0

# Input looks like below
# 2174368826: 4 3 39 14 2 4 8 3 7 4 711

def is_valid(target, numbs, operators):
    n_numbs = len(numbs)
    for option in itertools.product(operators, repeat = n_numbs-1):
        if len(operators) == 3 and '|' not in option:
            continue
        count = numbs[0]
        for idx, numb in enumerate(numbs[1:]):
            if count > target:
                break
            if option[idx] == '+': 
                count += numb
            elif option[idx] == '*':
                count *= numb
            elif option[idx] == '|':
                count = int(f"{count}{numb}")
        if count == target:
            return count
    return 0
 
for c, line in enumerate(D):
    if c%50 == 0:
        print(c)
    target, numbs = line.split(':')
    target = int(target)
    numbs = list(map(int, numbs.split()))
    operators = ('*', '+')
    succes = is_valid(target, numbs, operators)
    if succes:
        p1 += succes
        p2 += succes
    else:
        operators = ('*','+','|')
        p2 += is_valid(target, numbs, operators)

print(f"P1: {p1}")
print(f"P2: {p2}")
print(f"Execution Time: {time.time() - start_time:6f} seconds")
