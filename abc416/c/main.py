import itertools

n, k, x = map(int, input().split())

s = []
for i in range(n):
    s.append(input().strip())

patterns = []


for prod in itertools.product(range(n), repeat=k):
    temp = []
    for i in range(k):
        temp.append(s[prod[i]])
    patterns.append("".join(temp))

patterns.sort()

print(patterns[x - 1])
