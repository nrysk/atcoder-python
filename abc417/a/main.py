n, a, b = map(int, input().split())
s = input().strip()

print(s[a:-b] if b != 0 else s[a:])
