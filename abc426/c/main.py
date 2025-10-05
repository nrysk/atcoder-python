n, q = map(int, input().split())

cnt = [1] * (n + 1)


bottom_version = 1
for _ in range(q):
    x, y = map(int, input().split())
    if bottom_version > x:
        print(0)
    else:
        sum_cnt = sum(cnt[bottom_version : x + 1])
        print(sum_cnt)
        cnt[y] += sum_cnt
        bottom_version = max(bottom_version, x + 1)
