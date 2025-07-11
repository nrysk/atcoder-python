n, m = map(int, input().split())
a = list(map(int, input().split()))

if sum(a) > m:
    print("No")
else:
    print("Yes")
