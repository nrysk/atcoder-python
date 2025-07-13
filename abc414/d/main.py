n, m = map(int, input().split())
x = list(map(int, input().split()))
x = set(x)
x = list(x)
if len(x) <= m:
    print(0)
    exit()
x.sort()
max_dist = x[-1] - x[0]
dist = []
for i in range(len(x) - 1):
    dist.append((i, x[i + 1] - x[i]))
dist.sort(key=lambda x: x[1], reverse=True)
sum = 0
for i in range(m - 1):
    sum += dist[i][1]
print(max_dist - sum)
