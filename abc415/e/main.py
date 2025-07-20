h, w = map(int, input().split())

a = []
for _ in range(h):
    row = reversed(list((map(int, input().split()))))
    a.append(list(row))
a = list(reversed(a))
p = list(reversed(list(map(int, input().split()))))

required = [[0] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if i == 0 and j == 0:
            required[i][j] = p[i + j] - a[i][j]
        elif i == 0:
            required[i][j] = p[i + j] - a[i][j] + required[i][j - 1]
        elif j == 0:
            required[i][j] = p[i + j] - a[i][j] + required[i - 1][j]
        else:
            required[i][j] = (
                p[i + j] - a[i][j] + min(required[i - 1][j], required[i][j - 1])
            )
        # required[i][j]が負の値にならないようにする
        if required[i][j] < 0:
            required[i][j] = 0


print(required[h - 1][w - 1])
