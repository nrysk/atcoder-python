from itertools import permutations

n = int(input())
a = list(map(int, input().split()))

# 1からnまでの順列でるーぷする
for p in permutations(range(1, n + 1)):
    # pの各要素を出力する
    if all((a[i] == -1 or a[i] == p[i]) for i in range(n)):
        print("Yes")
        print(*p)
        break
else:
    print("No")
