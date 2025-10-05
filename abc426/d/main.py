import itertools

t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    # 0と1が連続する個数で圧縮する
    compressed = [len(list(g)) for _, g in itertools.groupby(s)]

    if len(compressed) == 1:
        print(0)
        continue

    # 偶数番目を2倍にしたときの最小コスト
    cost_sum = 0
    cost_max = 0
    for i, x in enumerate(compressed):
        if i % 2 == 0:
            cost_sum += x * 2
            cost_max = max(cost_max, x * 2)
        else:
            cost_sum += x
    ans = cost_sum - cost_max

    # 奇数番目を2倍にしたときの最小コスト
    cost_sum = 0
    cost_max = 0
    for i, x in enumerate(compressed):
        if i % 2 == 1:
            cost_sum += x * 2
            cost_max = max(cost_max, x * 2)
        else:
            cost_sum += x
    ans = min(ans, cost_sum - cost_max)
    print(ans)

    # # 偶数番目を2倍にした配列
    # doubled_even = [x * 2 if i % 2 == 0 else x for i, x in enumerate(compressed)]

    # # 奇数番目を2倍にした配列
    # doubled_odd = [x * 2 if i % 2 == 1 else x for i, x in enumerate(compressed)]

    # sum_even = sum(doubled_even)
    # max_even = max(doubled_even)
    # sum_odd = sum(doubled_odd)
    # max_odd = max(doubled_odd)

    # ans = min(sum_even - max_even, sum_odd - max_odd)
    # print(ans)
