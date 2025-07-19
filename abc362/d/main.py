import heapq

n, m = map(int, input().split())

a = list(map(int, input().split()))
edges = [[] for _ in range(2 * n)]
for i in range(n):
    edges[i].append((n + i, a[i]))
for i in range(m):
    u, v, b = map(int, input().split())
    u, v = u - 1, v - 1
    edges[n + u].append((v, b))
    edges[n + v].append((u, b))

pq = [(0, 0)]  # (dist, node)
dist = [float("inf")] * (2 * n)
dist[0] = 0

while pq:
    d, node = heapq.heappop(pq)
    if d > dist[node]:
        continue
    for next_node, weight in edges[node]:
        new_dist = d + weight
        if new_dist < dist[next_node]:
            dist[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))

print(" ".join(map(str, dist[n + 1 :])))
