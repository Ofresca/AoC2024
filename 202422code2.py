import time 
from collections import defaultdict

start_time = time.time()

with open("202422input.txt") as file: D = file.read().strip().split('\n')

D = list(map(int, D))

p1, p2 = 0, 0

def next_secret_number(secret_number: int) -> int:
    step_1 = (secret_number ^ (secret_number * 64)) % 16777216
    step_2 = (step_1 ^ (step_1 // 32)) % 16777216
    step_3 = (step_2 ^ (step_2 * 2048)) % 16777216
    return step_3

bananas = defaultdict(int)
for numb in D:
    seq = (0, )
    seen = set() # Can only add a sequence the first time you find it. 
    for _ in range(2000):
        last, numb = numb, next_secret_number(numb)
        seq = seq[-3:] + (numb % 10 - last % 10,)
        if len(seq) == 4:
            if seq not in seen: 
                seen.add(seq)
                bananas[seq] += numb % 10
    p1 += numb

p2 = max(bananas.values())

print(f"P1 = {p1}")
print(f"P2 = {p2}")
p2_time = time.time()
print(f"Total time = {p2_time - start_time:6f}")