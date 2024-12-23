import time 
from collections import defaultdict
from functools import cache

# ANS = [224326, 279638326609472]

start_time = time.time()

# Row, Column
DIR_TO_CHAR = {(-1, 0): '^', (0, 1): '>', (1, 0): 'v', (0, -1): '<', (0,0): ''}
DIR_KEYPAD = {'A': (0,2), '^': (0,1), '<': (1,0), 'v': (1,1), '>': (1,2)}
FINAL_KEYPAD_C2D = {
    'A': (3, 2), '0': (3, 1), 
    '1': (2,0), '2': (2,1), '3': (2,2), 
    '4': (1,0), '5': (1,1), '6': (1,2), 
    '7': (0,0), '8': (0,1), '9': (0,2)}

with open("202421input.txt") as file: 
    D = file.read().strip().split('\n')

p1, p2 = 0, 0

# Utility functions
def sign(num: int) -> int:
    """Returns the sign of the number: -1 for negative, 1 for positive, 0 for zero."""
    return (num > 0) - (num < 0)

def dirs_allowed_kp(cur_pos: tuple, end_pos: tuple): # Returns DIRS2
    """Returns valid direction steps based on keypad movement rules."""
    dir_r, dir_c = end_pos[0] - cur_pos[0], end_pos[1] - cur_pos[1]
    one_path_1 = {(0,0), (1,0), (2,0)} # 7 - 4 - 1 down
    one_path_2 = {(3,1), (3,2)} # 0 - A right
    if cur_pos in one_path_1 and end_pos in one_path_2:
        # One possible path 
        return 1, [((0, sign(dir_c)), (sign(dir_r), 0))]
    elif cur_pos in one_path_2 and end_pos in one_path_1:
        # One possible path 
        return 1, [((sign(dir_r), 0), (0, sign(dir_c)))]
    elif dir_r == 0 or dir_c == 0: 
        # One direction only 
        return 0, [((sign(dir_r), sign(dir_c)))]
    else: 
        # Two possible paths
        return 1, [((0, sign(dir_c)), (sign(dir_r), 0)), 
                ((sign(dir_r), 0), (0, sign(dir_c)))]

paths_kp = defaultdict(list)
# Create a cache of all possible paths between keypad points. 
for key_1 in FINAL_KEYPAD_C2D:
    for key_2 in FINAL_KEYPAD_C2D:
        if key_1 != key_2:
            s_pos = FINAL_KEYPAD_C2D[key_1]
            e_pos = FINAL_KEYPAD_C2D[key_2]
            dr = abs(e_pos[0] - s_pos[0])
            dc = abs(e_pos[1] - s_pos[1])
            drs, dirs2 = dirs_allowed_kp(s_pos, e_pos)
            if drs:    
                for dir1, dir2 in dirs2:
                    num_dir1 = dr if dir1[1] == 0 else dc
                    num_dir2 = dr if dir2[1] == 0 else dc
                    dir1 = DIR_TO_CHAR[dir1]
                    dir2 = DIR_TO_CHAR[dir2]
                    paths_kp[key_1, key_2] += [dir1*num_dir1 + dir2*num_dir2 + 'A']
            else: 
                dir1 = DIR_TO_CHAR[dirs2[0]]
                paths_kp[key_1, key_2] += [dir1*dr + dir1*dc + 'A']
        else: 
            paths_kp[key_1, key_2] = ['A']

# Simplified path finding for directional pad (similar to keypad above)
def dirs_allowed_dp(cur_pos: tuple, end_pos: tuple): # Returns DIRS2
    """Returns valid direction steps based on directional pad movement rules."""
    dir_r, dir_c = end_pos[0] - cur_pos[0], end_pos[1] - cur_pos[1]
    one_path_1 = {(0,1), (0,2)} # ^A 
    one_path_2 = {(1,0)} # <

    if cur_pos in one_path_1 and end_pos in one_path_2:
        # One possible path 
        return 1, [((sign(dir_r), 0), (0, sign(dir_c)))]
    elif cur_pos in one_path_2 and end_pos in one_path_1:
        # One possible path 
        return 1, [((0, sign(dir_c)), (sign(dir_r), 0))]
    elif dir_r == 0 or dir_c == 0: 
        # One direction only 
        return 0, [((sign(dir_r), sign(dir_c)))]
    else: 
        # Two possible paths
        return 1, [((0, sign(dir_c)), (sign(dir_r), 0)), 
                ((sign(dir_r), 0), (0, sign(dir_c)))]
            
paths_dp = defaultdict(list)
# Cache the movement paths for directional pad 
for key_1 in DIR_KEYPAD:
    for key_2 in DIR_KEYPAD:
        if key_1 != key_2:
            s_pos = DIR_KEYPAD[key_1]
            e_pos = DIR_KEYPAD[key_2]
            dr = abs(e_pos[0] - s_pos[0])
            dc = abs(e_pos[1] - s_pos[1])
            drs, dirs2 = dirs_allowed_dp(s_pos, e_pos)
            if drs:    
                for dir1, dir2 in dirs2:
                    num_dir1 = dr if dir1[1] == 0 else dc
                    num_dir2 = dr if dir2[1] == 0 else dc
                    dir1 = DIR_TO_CHAR[dir1]
                    dir2 = DIR_TO_CHAR[dir2]
                    paths_dp[key_1, key_2] += [dir1*num_dir1 + dir2*num_dir2 + 'A']
            else: 
                dir1 = DIR_TO_CHAR[dirs2[0]]
                paths_dp[key_1, key_2] += [dir1*dr + dir1*dc + 'A']
        else: 
            paths_dp[key_1, key_2] = ['A']

# Helper function to combine paths efficiently
def combine_lists(options_list: list) -> list:
    final_list = ['']
    for options in options_list:
        final_list = [f + option for f in final_list for option in options]
    return final_list

def buildSeq(keys):
    """Build the sequence of keys and corresponding paths."""
    options_dkp = [paths_dp[(key1, key2)] for key1, key2 in zip('A'+keys, keys)]
    return combine_lists(options_dkp)

@cache
def shortestSeq(keys: str, depth: int) -> int: # returns total length of keys
    total = 0
    if depth == 0:
        return len(keys)
    for key in keys.split('A')[:-1]:
        key_list = buildSeq(key+'A')
        total += min(shortestSeq(seq, depth-1) for seq in key_list)
    return total

for idx, line in enumerate(D):
    cp_fkp = 'A'
    options_fkp = [] 
    for char_fkp in line:
        options_fkp.append(paths_kp[(cp_fkp, char_fkp)])
        cp_fkp = char_fkp

    paths_fkp = combine_lists(options_fkp)

    seq_length = min(shortestSeq(path, 2) for path in paths_fkp)

    num_part = int(line[:3])
    complexity = seq_length * num_part
    p1 += complexity

print(f"P1 = {p1}")
p1_time = time.time()
print(f"P1 time = {p1_time - start_time:6f}")

for idx, line in enumerate(D):
    cp_fkp = 'A'
    options_fkp = [] 
    for char_fkp in line:
        options_fkp.append(paths_kp[(cp_fkp, char_fkp)])
        cp_fkp = char_fkp

    paths_fkp = combine_lists(options_fkp)
    seq_length = min(shortestSeq(path, 25) for path in paths_fkp)
    num_part = int(line[:3])
    complexity = seq_length * num_part
    p2 += complexity

print(f"P2 = {p2}")
p2_time = time.time()
print(f"P2 time = {p2_time - p1_time:6f}")
print(f"Total time = {p2_time - start_time:6f}")
