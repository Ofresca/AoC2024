import time

# ANS = [2885]

start_time = time.time()

# Open the file and read in the blocks of data
with open("202425input.txt") as file:
    D = file.read().strip().split('\n\n')

# Initialize variables
p1 = 0
locks, keys = [], []

# Process keys and locks
for item in D:
    item_lines = item.split('\n')
    transposed = list(zip(*item_lines))  # Transpose
    vals = [line.count('#') for line in transposed]
    if item_lines[0][0] == '.':  # Key
        keys.append(vals)
    else:  # Lock
        locks.append(vals)

# Compare lock and key values
p1 = sum(1 for lock in locks for key in keys if 
         all(l + k <= 7 for l, k in zip(lock, key)))

# Output results
print(f"P1 = {p1}")
print(f"Total time = {time.time() - start_time:6f}")