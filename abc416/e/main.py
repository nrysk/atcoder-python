import numpy as np

n, m = map(int, input().split())
dist = np.full((n + 1, n + 1), np.inf)

for _ in range(m):
    a, b, c = map(int, input().split())
    c *= 2
    dist[a][b] = min(dist[a][b], c)
    dist[b][a] = min(dist[b][a], c)
for i in range(n + 1):
    dist[i][i] = 0

k, hub_cost = map(int, input().split())
d = list(map(int, input().split()))
# dに含まれる頂点同士の距離はtである
# ハブとなる頂点0を追加する
for i in range(k):
    dist[0][d[i]] = hub_cost
    dist[d[i]][0] = hub_cost

# 初期状態のすべての頂点間の最短距離をフロイドワーシャル法で求める
for k in range(n + 1):
    for i in range(n + 1):
        for j in range(n + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

ans = []

q = int(input())
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x, y, t = query[1], query[2], query[3]
        # 頂点xとyの距離をtに更新する
        dist[x][y] = min(dist[x][y], t)
        dist[y][x] = min(dist[y][x], t)
        # 更新後の全ての頂点間の最短距離を再計
        for i in range(n + 1):
            for j in range(n + 1):
                dist[i][j] = min(dist[i][j], dist[i][x] + t + dist[y][j])
                dist[i][j] = min(dist[i][j], dist[i][y] + t + dist[x][j])
    elif query[0] == 2:
        x = query[1]
        # 頂点xをハブ頂点に接続する
        dist[0][x] = hub_cost
        dist[x][0] = hub_cost
        # ハブ頂点と頂点xを通る全ての頂点間の距離を更新する
        for i in range(n + 1):
            for j in range(n + 1):
                dist[i][j] = min(dist[i][j], dist[i][0] + hub_cost + dist[x][j])
                dist[i][j] = min(dist[i][j], dist[i][x] + hub_cost + dist[0][j])
    elif query[0] == 3:
        # 全ての頂点間の最短距離の総和を再計算する
        # total_distance = sum(
        #     dist[i][j]
        #     for i in range(1, n + 1)
        #     for j in range(1, n + 1)
        #     if dist[i][j] < float("inf")
        # )
        total_distance = np.sum(
            dist[1 : n + 1, 1 : n + 1][dist[1 : n + 1, 1 : n + 1] < np.inf]
        )
        # from pprint import pprint

        # pprint(dist)
        ans.append(int(total_distance))

print("\n".join(map(str, ans)))
