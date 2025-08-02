from collections import Counter

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b = Counter(b)

for i in range(n):
    if a[i] in b:
        if b[a[i]] > 0:
            b[a[i]] -= 1
            continue
    print(a[i], end=" ")
