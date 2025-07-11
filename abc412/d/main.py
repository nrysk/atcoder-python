from itertools import permutations

n, m = map(int, input().split())
edges = set()
for _ in range(m):
    a, b = map(int, input().split())
    edges.add((a - 1, b - 1))
    edges.add((b - 1, a - 1))
num_edges = len(edges) // 2
nodes_str = "".join(str(i) for i in range(n)) + "|"
perm = permutations(nodes_str)


def count_edges_in_route(route: str) -> tuple[int, int]:
    count = 0
    lack_count = 0
    for i in range(len(route) - 1):
        if (int(route[i]), int(route[i + 1])) in edges or (
            int(route[i + 1]),
            int(route[i]),
        ) in edges:
            count += 1
        else:
            lack_count += 1
    return count, lack_count


min_cost = float("inf")
for p in perm:
    groups = "".join(p).split("|")
    # 片方のノード数が1か2の場合はcontinue
    if len(groups[0]) in [1, 2] or len(groups[1]) in [1, 2]:
        continue

    # 一つのグループになる場合
    if len(groups[0]) == n:
        count, lack_count = count_edges_in_route(groups[0] + groups[0][0])
        costs = num_edges - count + lack_count
    elif len(groups[1]) == n:
        count, lack_count = count_edges_in_route(groups[1] + groups[1][0])
        costs = num_edges - count + lack_count
    else:
        count1, lack_count1 = count_edges_in_route(groups[0] + groups[0][0])
        count2, lack_count2 = count_edges_in_route(groups[1] + groups[1][0])
        costs = num_edges - (count1 + count2) + (lack_count1 + lack_count2)

    min_cost = min(min_cost, costs)

print(min_cost)
