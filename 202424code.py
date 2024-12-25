import time 

# ANS = [53190357879014, bks,hnd,nrn,tdv,tjp,z09,z16,z23]

start_time = time.time()

with open("202424input.txt") as file: D = file.read().strip().split('\n\n')

gates = [line.split() for line in D[1].split('\n')]
states = {x: int(y) for x,y in (line.split(': ') for line in D[0].split('\n'))}
states.update({z[-1]: None for z in gates})

for state in states:
    if state.startswith('x'):
        states[state] = 0
    elif state.startswith('y'): 
        states[state] = 1

# Initialize final states as a dictionary
final_states = {state: None for state in states if state.startswith('z')}

def check_gate(x: str, y: str, com: str) -> int:
    if states[x] == None or states[y] == None:
        return None
    match com:
        case 'AND': return int(states[x] and states[y])
        case 'OR': return int(states[x] or states[y])
        case 'XOR': return int(states[x] ^ states[y])

# Process gates and update states
# Note: All variables are asigned only once. 
while any(z is None for z in final_states.values()):
    for x, operation, y, _, z in gates:
        if states.get(z) is None:
            result = check_gate(x, y, operation)
            if result is not None:
                states[z] = result
                if z.startswith('z'):
                    final_states[z] = result

# Prepare the result for P1 by reading final states in reverse order
p1_bin = ''.join(str(states[state]) for state in sorted(final_states, reverse=True))
print(p1_bin)
p1 = int(p1_bin, 2)

print(f"P1 = {p1}")
p1_time = time.time()
# print(f"P1 time = {p1_time - start_time:6f}")

states = {x: int(y) for x,y in (line.split(': ') for line in D[0].split('\n'))}
states.update({z[-1]: None for z in gates})
x_states = {x: y for x,y in states.items() if x.startswith('x')}
y_states = {x: y for x,y in states.items() if x.startswith('y')}

all_gates = dict()
z_gates = dict()
incorrect_states = {'z09', 'z23', 'hnd', 'z16', 'tdv', 'bks', 'tjp', 'nrn'}

for x,cmd,y,_,z in gates:
    all_gates[z] = (x, cmd, y)
    if z.startswith('z'):
        z_gates[z] = (x, cmd, y)

c_gates = dict()
r_gates = dict()
a_gates = dict()
d_gates = dict()

for key, value in sorted(z_gates.items()):
    cg, rg, ag, dg = False, False, False, False
    rnumb = int(key[1:]) # zXX -> Keep XX only
    numb = key[1:]
    x, cmd, y = value
    if rnumb == 0:
        for key1, value1 in all_gates.items():
            if {x,y,'AND'} == set(value1):
                c_gates[rnumb] = key1
                cg = True
    elif rnumb == 45:
        continue
    else:
        xr, yr = 'x'+numb, 'y'+numb
        for key2, value2 in all_gates.items():
            if {xr, yr, 'XOR'} == set(value2):
                r_gates[rnumb] = key2
                rg = True
            if {xr, yr, 'AND'} == set(value2):
                a_gates[rnumb] = key2
                ag = True
        if set(value) != {r_gates[rnumb], c_gates[rnumb-1], 'XOR'}:
            incorrect_states.add((key, 'XOR', r_gates[rnumb], c_gates[rnumb-1]))
        c, r = c_gates[rnumb-1], r_gates[rnumb]
        for key3, value3 in all_gates.items():
            if {c,r,'AND'} == set(value3):
                d_gates[rnumb] = key3
                dg = True
        for key4, value4 in all_gates.items():
            if {a_gates[rnumb], d_gates[rnumb], 'OR'} == set(value4):
                c_gates[rnumb] = key4
                cg = True
        if not all((cg, dg, ag, rg)):
            print(f"{cg=}, {dg=}, {ag=}, {rg=}")
            if not cg:
                print(f"{a_gates[rnumb]=}, {d_gates[rnumb]=}")
            if not dg:
                print(f"{c_gates[rnumb-1]=}, {r_gates[rnumb]=}")
            if not ag:
                print(f"{c_gates[rnumb-1]=}, {r_gates[rnumb]=}")
            
print(','.join(sorted(incorrect_states)))

    # x = all_gates[x]
    # y = all_gates[y]

# print(sorted(z_gates.items()))

'what do you get if you sort the names of the eight wires involved in a swap and then join those names with commas?'



p2 = 0
print(f"P2 = {p2}")
p2_time = time.time()
# print(f"P2 time = {p2_time - p1_time:6f}")
# print(f"Total time = {p2_time - start_time:6f}")
