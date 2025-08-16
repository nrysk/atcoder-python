n, m, l = map(int, input().split())
a = list(map(int, input().split()))


total_operations = 0
for i in range(l):
    chain_remainders = []
    for j in range(i, n, l):
        chain_remainders.append(a[j] % m)

    if not chain_remainders:
        continue

    chain_remainders.sort()
    k = len(chain_remainders)

    total_sum = sum(chain_remainders)

    prefix_sum = [0] * (k + 1)
    for idx in range(k):
        prefix_sum[idx + 1] = prefix_sum[idx] + chain_remainders[idx]

    min_chain_cost = float("inf")

    for p in range(k):
        target_r = chain_remainders[p]

        cost_le = (p + 1) * target_r - prefix_sum[p + 1]

        cost_gt = (
            (k - 1 - p) * m + (k - 1 - p) * target_r - (total_sum - prefix_sum[p + 1])
        )

        current_cost = cost_le + cost_gt
        min_chain_cost = min(min_chain_cost, current_cost)

    total_operations += min_chain_cost

if total_operations == 0:
    print("O")
else:
    print(total_operations)
