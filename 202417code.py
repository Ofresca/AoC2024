import time
import re

# ANS = [[3,7,1,7,2,1,0,6,3], 37221334433268]

start_time = time.time()

with open("202417input.txt") as file: D = file.read().strip()

a, b, c, *program = map(int, re.findall(r'\d+', D))

def value_opcode(a,b,c):
    ip, result = 0, []
    while ip < len(program):
        C = {0:0, 1:1, 2:2, 3:3, 4:a, 5:b, 6:c}
        code, rand = program[ip], program[ip+1]
        match code: 
            case 0:
                a = a >> C[rand] # = int(a / (2 ** C[rand]))
            case 1:
                b = b ^ rand
            case 2:
                b = 7 & C[rand]
            case 3:
                if a: ip = rand - 2 # Jump if a != 0
            case 4:
                b = b ^ c
            case 5:
                result += [C[rand] % 8]
            case 6:
                b = a >> C[rand]
            case 7:
                c = a >> C[rand]
        ip += 2
    return result

p1 = value_opcode(a, b, c)

print(f"P1 = {p1}")
p1_time = time.time()
print(f"P1 time = {p1_time - start_time:6f}")

# Convert a 3 bit number to int. 
# Output should be: 2,4,1,2,7,5,1,3,4,3,5,5,0,3,3,0
# Which is == program. 

p2 = 1e15
todo = [(1, 0)]
for i, a in todo:
    for na in range(a, a+8):
        if value_opcode(na, 0, 0) == program[-i:]:
            todo += [(i+1, na*8)]
            if i == len(program):
                print(na)
                p2 = min(na, p2)
                # todo.clear()
                break

print(f"P2 = {p2}")
p2_time = time.time()
print(f"P2 time = {p2_time - p1_time:6f}")
print(f"Total time = {p2_time - start_time:6f}")

