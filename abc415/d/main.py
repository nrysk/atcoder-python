n, m = map(int, input().split())

dec_amounts = []
for m in range(m):
    a, b = map(int, input().split())
    dec_amounts.append((a - b, a))  # (減少数, 必要個数)

# なるべく減少回数を多くする様にnを減らす
dec_amounts.sort()
cnt = 0
for dec, amount in dec_amounts:
    if n >= amount:
        diff = n - amount
        tmp = diff // dec + 1
        cnt += tmp
        n -= tmp * dec

print(cnt)
