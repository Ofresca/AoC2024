from collections import Counter

D = open("202401input.txt").read().split('\n')

firstlist, secondlist = [], []

for line in D:
    first, second = map(int, line.split())
    firstlist.append(first)
    secondlist.append(second)

firstlist.sort()
secondlist.sort()

p1 = p2 = 0

for first, second in zip(firstlist, secondlist):
    p1 += abs(first - second)
    p2 += secondlist.count(first) * first

secondCounter = Counter(secondlist)
p1 = sum(abs(left - right) for left, right in zip(firstlist,secondlist))
p2 = sum(left * secondCounter[left] for left in firstlist)

print(p1)
print(p2)
