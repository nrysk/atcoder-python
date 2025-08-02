from bisect import bisect_left

n = int(input())
p, a, b = [], [], []
for i in range(n):
    tmp_p, tmp_a, tmp_b = map(int, input().split())
    p.append(tmp_p)
    a.append(tmp_a)
    b.append(tmp_b)

b_cumsum = [b[0]]
for i in range(1, n):
    b_cumsum.append(b_cumsum[i - 1] + b[i])

p_limit = 1000
# 事前計算
dp = [
    [0] * (p_limit + 1) for _ in range(n + 1)
]  # [i][j] i番目を受け取ったときのテンションがjのときの最終テンション
for i in range((p_limit + 1)):
    # dp のための番兵
    dp[n][i] = i

for i in reversed(range(n)):
    for j in range((p_limit + 1)):
        if p[i] >= j:
            dp[i][j] = dp[i + 1][j + a[i]]
        else:
            if j - b[i] < 0:
                dp[i][j] = dp[i + 1][0]
            else:
                dp[i][j] = dp[i + 1][j - b[i]]


q = int(input())

for _ in range(q):
    x = int(input())
    # xが1000以下のときはそのまま出力
    if x <= p_limit:
        print(dp[0][x])
    else:
        # 最初にx-1000以上になるインデックスをb_cumsumから探す
        idx = bisect_left(b_cumsum, x - 1000)
        if idx == n:
            print(x - b_cumsum[n - 1])
            continue
        # そのインデックス以降のdpを使う
        print(dp[idx + 1][x - b_cumsum[idx]])
