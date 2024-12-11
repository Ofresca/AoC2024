import time 
from functools import cache

start_time = time.time()

ANS = [204022, 241651071960597]

with open("202411input.txt") as file: D = file.read().split()

stones = list(map(int, D))
p1, p2 = 0, 0 

@cache # @cache = @lru_cache(None)
def stone_changes(stone, n):
    # After depth = n
    if n == 0:
        return 1
    # First rule: If 0 -> 1
    if stone == 0:
        return stone_changes(1, n-1)
    # Second rule if even length, split numbers
    elif (l_stone := len(str(stone))) % 2 == 0:
        div_stone = 10 ** (l_stone // 2)
        return stone_changes((stone // div_stone), n-1) + stone_changes((stone % div_stone), n-1)
    # Else: multiply by 2024
    return stone_changes(stone * 2024, n-1)

# Run 25 times for P1
p1 = sum(stone_changes(stone, 25) for stone in stones)
print(f"P1 = {p1}")

p1_time = time.time()
print(f"P1 time = {p1_time - start_time:6f} s")

# Run 75 times for P2
p2 = sum(stone_changes(stone, 75) for stone in stones)
print(f"P2 = {p2}")

p2_time = time.time()
print(f"P2 time = {p2_time - p1_time:6f} s")
print(f"Total time = {p2_time - start_time:6f} s")