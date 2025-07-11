n, w = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[-1] * (w + 1) for _ in range(n + 1)]
dp[0][w] = 0

max_value = 0
for i in range(n):
    for j in range(w + 1):
        if dp[i][j] == -1:
            continue
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        if j >= items[i][0]:
            dp[i + 1][j - items[i][0]] = max(
                dp[i + 1][j - items[i][0]], dp[i][j] + items[i][1]
            )
            max_value = max(max_value, dp[i + 1][j - items[i][0]])

print(max_value)
