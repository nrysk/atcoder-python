import heapq

pq = []

q = int(input())

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        heapq.heappush(pq, query[1])
    elif query[0] == 2:
        min_value = heapq.heappop(pq)
        print(min_value)
