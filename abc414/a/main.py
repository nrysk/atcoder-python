n, l, r = map(int, input().split())

cnt = 0
for i in range(n):
    x, y = map(int, input().split())
    if x <= l and y >= r:
        cnt += 1

print(cnt)
