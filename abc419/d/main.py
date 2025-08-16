n, m = map(int, input().split())
s = input()
t = input()

swap_map = [False] * (n + 1)

for i in range(m):
    l, r = map(int, input().split())
    swap_map[l - 1] = not swap_map[l - 1]
    swap_map[r] = not swap_map[r]

string_builder = []
need_swap = False
for i in range(n):
    if swap_map[i]:
        need_swap = not need_swap

    if need_swap:
        string_builder.append(t[i])
    else:
        string_builder.append(s[i])

print("".join(string_builder))
