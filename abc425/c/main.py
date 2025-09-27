n, q = map(int, input().split())
a = list(map(int, input().split()))
# aとaを連結する
a += a

sum_to_i = [0] * (2 * n + 1)
for i in range(1, 2 * n + 1):
    sum_to_i[i] = sum_to_i[i - 1] + a[i - 1]

offset = 0
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        offset = (offset +  query[1]) % n
    else:
        l, r = query[1] - 1, query[2] - 1
        print(sum_to_i[offset + r + 1] - sum_to_i[offset + l])
