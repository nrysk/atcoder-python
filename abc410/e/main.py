n, h, m = map(int, input().split())

dp = [[-1] * (h + 1) for _ in range(n + 1)]
dp[0][h] = m
ans = 0
for i in range(n):
    a, b = map(int, input().split())
    flg = False
    for i_h in range(h + 1):
        if dp[i][i_h] == -1:
            continue
        if i_h - a >= 0:
            dp[i + 1][i_h - a] = max(dp[i + 1][i_h - a], dp[i][i_h])
            flg = True
        if dp[i][i_h] - b >= 0:
            dp[i + 1][i_h] = max(dp[i + 1][i_h], dp[i][i_h] - b)
            flg = True
    if flg:
        ans = i + 1

print(ans)
