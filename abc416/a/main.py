n, l, r = map(int, input().split())
s = input().strip()

if all(c == "o" for c in s[l - 1 : r]):
    print("Yes")
else:
    print("No")
