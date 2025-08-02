from collections import Counter

n = int(input())
a = list(map(int, input().split()))

values1 = [(i + 1) - a[i] for i in range(n)]
values2 = [(i + 1) + a[i] for i in range(n)]

values1_count = Counter(values1)
values2_count = Counter(values2)

# 一致する組み合わせ数を計算
ans = 0
for value, count in values1_count.items():
    if value in values2_count:
        ans += count * values2_count[value]


print(ans)
