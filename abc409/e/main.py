from collections import deque

n = int(input())
x = list(map(int, input().split()))
edges = [[] for _ in range(n)]
for i in range(n - 1):
    u, v, w = map(int, input().split())
    edges[u - 1].append((v - 1, w))
    edges[v - 1].append((u - 1, w))

degrees = [len(edges[i]) for i in range(n)]
deleted = [False] * n
queue = deque()

for i in range(n):
    if degrees[i] == 1:
        queue.append(i)

cost = 0
while queue:
    node = queue.popleft()
    deleted[node] = True
    # 隣接ノードは1つに限られる
    for neighbor, weight in edges[node]:
        if deleted[neighbor]:
            continue
        degrees[neighbor] -= 1
        if degrees[neighbor] == 1:
            queue.append(neighbor)
        x[neighbor] += x[node]
        cost += weight * abs(x[node])
        x[node] = 0

print(cost)
