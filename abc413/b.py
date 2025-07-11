n = int(input())
s = [input().strip() for _ in range(n)]


patterns = set()

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        patterns.add(s[i] + s[j])

print(len(patterns))
