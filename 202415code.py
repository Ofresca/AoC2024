import time 

start_time = time.time()

ANS = [1413675, 1399772]

with open("202415input.txt") as file: D = file.read().strip().split('\n\n')

# robot (@) - boxes (O) - wall (#), 
# ^ for up, v for down, < for left, > for right

DIRS4 = {'^': (-1, 0), '>': (0, 1),'v': (1, 0), '<': (0, -1)}
# print(DIRS4)
# Directions: up, right, down, left

grid = D[0].split('\n')
moves = D[1].replace('\n','')

####### P1 #######

grid_dict = {'#': [], 'O': [], '@': []}
n_r, n_c = len(grid), len(grid[0])

# Locations per item type. 
for r, line in enumerate(grid):
    for c, char in enumerate(line):
        if char != '.':
            grid_dict[char].append((r,c))

def visualize_grid_dict(positions, ncols, nrows):
    # Create a grid where empty positions are filled with '.'
    gridk = [['.' for _ in range(ncols)] for _ in range(nrows)]
    # Mark specified positions with '#'
    for tag, poss in positions.items():
        for pos in poss:
            r, c = pos
            gridk[r][c] = tag
    print('\n'.join(''.join(row) for row in gridk))

for char in moves:
    (dr, dc) = DIRS4[char]
    walls = grid_dict['#'] # Wall positions
    boxes = grid_dict['O'] # Box positions
    robot_pos = grid_dict['@'][0] # Extract robot positions
    r,c = robot_pos
    n_rp = (nr, nc) = (r+dr, c+dc)
    if n_rp in walls: 
        continue # Do nothing if the next position is a wall 
    elif n_rp in boxes: 
        # Move the boxes if possible 
        idx = 1
        while True:
            sr, sc = nr+idx*dr, nc+idx*dc
            if (sr, sc) in boxes:
                # Find the first non-stone
                idx += 1
                continue
            else:
                if (sr, sc) in walls:
                    # Do nothing if the next position is a wall
                    break
                else:
                    # update the locations
                    grid_dict['@'] = [n_rp]
                    grid_dict['O'].remove((nr,nc))
                    grid_dict['O'].append((sr,sc))
                    break
    else:
        grid_dict['@'] = [(nr, nc)]

p1 = sum(r*100 + c for (r,c) in grid_dict['O'])

print(f"P1 = {p1}")
p1_time = time.time()
print(f"P1 time = {p1_time - start_time:6f}")


####### P2 #######

n_r, n_c = len(grid), len(grid[0])*2

walls, boxes = [],[]

# Locations per item type. 
for r, line in enumerate(grid):
    for c, char in enumerate(line):
        if char == '#':
            walls.append(((r,2*c),(r,2*c+1)))
        elif char == 'O':
            boxes.append(((r,2*c),(r,2*c+1)))
        elif char == '@':
            robot = (r, 2*c)

def visualize_grid(robot, stones, walls, ncols, nrows):
    # Create a grid where empty positions are filled with '.'
    gridk = [['.' for _ in range(ncols)] for _ in range(nrows)]
    # Mark robot with @
    gridk[robot[0]][robot[1]] = '@'
    # Mark walls with '#'
    for poss in walls:
        for pos in poss:
            gridk[pos[0]][pos[1]] = '#'
    # Mark stones with []
    for (pos1,pos2) in stones:
        gridk[pos1[0]][pos1[1]] = '['
        gridk[pos2[0]][pos2[1]] = ']'
    print('\n'.join(''.join(row) for row in gridk))

def is_in(pos, blocks):
    for block in blocks:
        if pos in block:
            return block
    return False

for char in moves:
    (dr, dc) = DIRS4[char]
    (r,c) = robot
    n_pos = (r+dr, c+dc)
    
    if is_in(n_pos, walls): 
        continue # Hit a wall
    elif s_pos := is_in(n_pos, boxes):
        queue = [s_pos]
        seen, to_move = set(), set()
        can_move = True
        while queue:
            stone_check = queue.pop()
            if stone_check in seen:
                continue
            seen.add(stone_check)
            to_move.add(stone_check)
            ((r1, c1), (r2,c2)) = stone_check
            sr1, sc1 = r1+dr, c1+dc
            sr2, sc2 = r2+dr, c2+dc
            sr_new = ((sr1, sc1),(sr2,sc2))
            for pos in sr_new:
                if ss := is_in(pos, boxes):
                    to_move.add(ss)
                    queue.append(ss)
                    continue
                else:
                    if is_in(pos, walls):
                        can_move = False
                        queue = []
                        break
        # Update the locations
        if can_move:
            robot = n_pos
            for pos in to_move:
                ((r1,c1),(r2,c2)) = pos
                boxes.remove((pos))
                boxes.append(((r1+dr,c1+dc),(r2+dr,c2+dc)))
    else:
        robot = n_pos # Hit nothing, just move. 

p2 = sum(min(r1, r2)*100 + min(c1, c2) for (r1,c1),(r2,c2) in boxes)

print(f"P2 = {p2}")
p2_time = time.time()
print(f"P2 time = {p2_time - p1_time:6f}")
print(f"Total time = {p2_time - start_time:6f}")
