import math

n = int(input())

r, c = [], []
for _ in range(n):
    tmp_r, tmp_c = map(int, input().split())
    r.append(tmp_r)
    c.append(tmp_c)

min_r = min(r)
max_r = max(r)
min_c = min(c)
max_c = max(c)

max_diff = max(max_r - min_r, max_c - min_c)
print(math.ceil(max_diff / 2))
