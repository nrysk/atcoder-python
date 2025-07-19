import heapq

n, m = map(int, input().split())
edges = [[] for _ in range(3 * n)]
for i in range(m):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    edges[u].append(v + n)
    edges[u + n].append(v + 2 * n)
    edges[u + 2 * n].append(v)

s, t = map(int, input().split())
s, t = s - 1, t - 1

dist = [float("inf")] * (3 * n)
dist[s] = 0
pq = [(0, s)]  # (dist, node)

while pq:
    d, node = heapq.heappop(pq)
    if d > dist[node]:
        continue
    for next_node in edges[node]:
        new_dist = d + 1
        if new_dist < dist[next_node]:
            dist[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))

if dist[t] == float("inf"):
    print(-1)
else:
    print(dist[t] // 3)
