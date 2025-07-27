t = int(input())


def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort(reverse=True)

    pairs = []
    i_b = 0
    for i_a in range(n):
        if a[i_a] + b[i_b] >= m:
            pairs.append((i_a, i_b))
            i_b += 1
        if i_b >= n:
            break

    sum_value = sum(a) + sum(b)
    sum_value -= len(pairs) * m

    print(sum_value)


for _ in range(t):
    solve()
