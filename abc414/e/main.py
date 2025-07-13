n = int(input())


def sum_floor(n):
    if n == 0:
        return 0
    sqrt_n = int(n**0.5)

    sum = 0
    for i in range(1, sqrt_n + 1):
        sum += n // i
    return sum * 2 - sqrt_n * sqrt_n


ans = n * (n + 1) // 2 - sum_floor(n)
print(ans % 998244353)
