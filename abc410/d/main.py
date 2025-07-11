from collections import deque

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b, w = map(int, input().split())
    edges[a - 1].append((b - 1, w))

table = set()
queue = deque([(0, 0)])  # (node, cost)
while queue:
    node, cost = queue.popleft()
    for next_node, next_weight in edges[node]:
        next_cost = cost ^ next_weight
        if (next_node, next_cost) in table:
            continue
        table.add((next_node, next_cost))
        queue.append((next_node, next_cost))

min_cost = float("inf")
for node, cost in table:
    if node == n - 1:
        min_cost = min(min_cost, cost)

if min_cost == float("inf"):
    print(-1)
else:
    print(min_cost)
