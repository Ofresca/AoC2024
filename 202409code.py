import time

# ANS = [6259790630969, 6289564433984]

start_time = time.time()

with open("202409input.txt") as file: D = file.read()

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

D = [int(numb) for numb in D]+[0]

for idx, numb in enumerate(D):
    if idx%2 == 0:
        for _ in range(numb):
            disk_map.append(int(idx/2))
    else:
        for _ in range(numb):
            disk_map.append('.')

while '.' in disk_map:
    idx = disk_map.index('.')
    move_file = disk_map.pop()
    if move_file == '.':
        continue
    else:
        disk_map[idx] = move_file

p1 = sum(file*idx for idx, file in enumerate(list(disk_map)))

print(f"P1 = {p1}")
p1_time = time.time()
print(f"Time for P1 = {p1_time-start_time:6f}")

files, empties = [], []
for idx, numb in enumerate(D):
    if idx%2 == 0:
        files.append((numb, int(idx/2)))
    else:
        empties.append(numb)

n_files = files.copy()

for (file, loc) in reversed(files):
    old_index = n_files.index((file,loc))
    for jdx, space in enumerate(empties[:old_index]):
        if 0 < file <= space:
            n_files.insert(jdx+1, n_files.pop(old_index))
            empties = empties[:old_index-1] + [empties[old_index-1]+empties[old_index]+file] + empties[old_index+1:]
            empties.insert(jdx, empties[jdx] - file)
            empties.pop(jdx+1)
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
