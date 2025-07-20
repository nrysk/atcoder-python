from collections import deque

h, w = map(int, input().split())

s = []
for _ in range(h):
    s.append(input())

# 'S' と 'G' の位置を特定
start = None
goal = None
for i in range(h):
    for j in range(w):
        if s[i][j] == "S":
            start = (i, j)
        elif s[i][j] == "G":
            goal = (i, j)

visited = set()  # (x, y, dir)
queue = deque(
    [(start[0], start[1], 0, 0), (start[0], start[1], 1, 0)]
)  # (x, y, dir, distance)

while queue:
    x, y, dir, dist = queue.popleft()
    # print(f"Visiting: ({x}, {y}), Direction: {dir}, Distance: {dist}")
    if (x, y) == goal:
        print(dist)
        exit()
    if (x, y, dir) in visited:
        continue
    visited.add((x, y, dir))

    if dir == 0:
        for dx in [-1, 1]:
            nx, ny = x + dx, y
            if 0 <= nx < h and 0 <= ny < w and s[nx][ny] != "#":
                queue.append((nx, ny, 1, dist + 1))
    else:
        for dy in [-1, 1]:
            nx, ny = x, y + dy
            if 0 <= nx < h and 0 <= ny < w and s[nx][ny] != "#":
                queue.append((nx, ny, 0, dist + 1))

print(-1)
