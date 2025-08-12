from collections import defaultdict
from math import gcd

n = int(input())
x, y = [], []
for _ in range(n):
    tmp_x, tmp_y = map(int, input().split())
    x.append(tmp_x)
    y.append(tmp_y)

trapezoidal_count = 0
parallelogram_count = 0
slope_count_dict = defaultdict(int)
slope_length_count_dict = defaultdict(int)
for i in range(n):
    for j in range(i + 1, n):
        dx = x[j] - x[i]
        dy = y[j] - y[i]
        if dx == 0:
            slope = "inf"
        else:
            common_gcd = abs(gcd(dx, dy))
            if dx < 0:
                dx, dy = -dx, -dy
            if dy == 0:
                slope = (0, 1)
            else:
                slope = (dy // common_gcd, dx // common_gcd)
        trapezoidal_count += slope_count_dict[slope]
        parallelogram_count += slope_length_count_dict[(slope, dx**2 + dy**2)]
        slope_count_dict[slope] += 1
        slope_length_count_dict[(slope, dx**2 + dy**2)] += 1
print(trapezoidal_count - parallelogram_count // 2)
