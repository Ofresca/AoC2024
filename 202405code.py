from collections import defaultdict

D = open("202405input.txt").read().split('\n\n')

rules = D[0].split('\n')
updates = D[1].split('\n')

rule_dict = defaultdict(list)
p1 = p2 = 0

for rule in rules: 
    before, after = rule.split('|')
    rule_dict[before].append(after)

for update in updates:
    correct = True
    book = update.split(',')
    for i, page in enumerate(book[1:],1):
        if set(book[:i]) & set(rule_dict[page]):
            correct = False
            break
    middleIndex = int((len(book)-1)/2)
    p1 += int(book[middleIndex])*correct
    if not correct:
        newlist = []
        while book:
            for page in book: 
                if not any(page in rule_dict[i] for i in book):
                    newlist.append(page)
                    book.remove(page)
        p2 += int(newlist[middleIndex])

print(p1)
print(p2)