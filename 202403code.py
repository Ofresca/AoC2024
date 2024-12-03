import re

D = open("202403in.txt").read()

p1 = p2 = 0
on = True

# xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))

# Regular expression 
# Here we go

pattern = r'mul\((\d+),(\d+)\)'
p1 = sum(int(a)*int(b) for a,b in re.findall(pattern,D))
print(p1)

for a,b,do,dont in re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", D):
    if do or dont:
        on = bool(do)
    else:
        p2 += int(a)*int(b)*on

print(p2)

p2 = 0 
sections_do = re.split('do\\(\\)', D)
for section_do in sections_do:
    section_dont = re.split('don\'t\\(\\)', section_do)
    matches = re.findall(pattern, section_dont[0])
    for a,b in matches:
        p2 += int(a)*int(b)

print(p2)
