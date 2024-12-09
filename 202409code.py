import time

# ANS = [6259790630969, 6289564433984]

start_time = time.time()

with open("202409input.txt") as file: D = file.read()

# Function to print the string, great for debugging. 
def print_disk_map(files, empties):
    disk_map = ""
    for file, empty in zip(files,empties):
        idx, numb = file
        for _ in range(idx):
            disk_map += str(numb)
        if empty > 0:
            for _ in range(empty):
                disk_map += str('.')
    print(disk_map)

p1, p2 = 0, 0
disk_map = []

# Add in sneaky extra zero
D = [int(numb) for numb in D]+[0]

# Generate disk_map by creating the string
for idx, numb in enumerate(D):
    if idx%2 == 0:
        for _ in range(numb):
            disk_map.append(int(idx/2))
    else:
        for _ in range(numb):
            disk_map.append('.')

# Move files from the back of the string to the front. 
while '.' in disk_map:
    idx = disk_map.index('.')
    move_file = disk_map.pop()
    if move_file != '.':
        disk_map[idx] = move_file

p1 = sum(file*idx for idx, file in enumerate(list(disk_map)))

print(f"P1 = {p1}")
p1_time = time.time()
print(f"Time for P1 = {p1_time-start_time:6f}")

files, empties = [], []
# Create two lists, one with files and numbers, one with locations of empties
for idx, numb in enumerate(D):
    if idx%2 == 0:
        files.append((numb, int(idx/2)))
    else:
        empties.append(numb)

n_files = files.copy()

# Move files from the back of the list to the front. 
for (file, loc) in reversed(files):
    old_index = n_files.index((file,loc))
    for jdx, space in enumerate(empties[:old_index]):
        if 0 < file <= space:
            # Insert at new location and remove from old for file overview
            n_files.insert(jdx+1, n_files.pop(old_index))
            # Remove from old location by adding before, length, after
            empties = empties[:old_index-1] + [empties[old_index-1]+empties[old_index]+file] + empties[old_index+1:]
            # Insert at new location for length empty - file
            empties.insert(jdx, empties[jdx] - file)
            # Remove old location
            empties.pop(jdx+1)
            # Insert first location = 0. 
            empties.insert(jdx, 0)
            break

# print_disk_map(n_files, empties)

# Calculate the P2 answer by calculating the checksum
step = 0
for (file, loc), empty in zip(n_files, empties):
    for _ in range(file):
        p2 += loc*step
        step += 1
    step += empty

print(f"P2: {p2}")

p2_time = time.time()
print(f"Time for P2 = {p2_time-p1_time:6f}s")
print(f"Total time = {p2_time - start_time:6f}s")
