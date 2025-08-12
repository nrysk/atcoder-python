n = int(input())
t = input().strip()

dp = [[0] * 2 for _ in range(n + 1)]

for i in range(n):
    if t[i] == "0":
        dp[i][0] = dp[i - 1][1] + 1
        dp[i][1] = dp[i - 1][0]
    else:
        dp[i][0] = dp[i - 1][0]
        dp[i][1] = dp[i - 1][1] + 1

sum = 0
for i in range(n):
    sum += dp[i][1]

print(sum)
