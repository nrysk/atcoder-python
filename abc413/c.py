from collections import deque

q = int(input())

a = deque()

for _ in range(q):
    query = input().split()

    if query[0] == "1":
        c = int(query[1])
        x = int(query[2])

        a.append((c, x))

    else:
        k = int(query[1])

        sum = 0
        while k > 0:
            c, x = a.popleft()
            if k >= c:
                sum += c * x
                k -= c
            else:
                sum += k * x
                a.appendleft((c - k, x))
                k = 0

        print(sum)
