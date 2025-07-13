n = int(input())

length = 0
string_buffer = []
for i in range(n):
    c, l = input().split()
    l = int(l)
    length += l
    if length > 100:
        print("Too Long")
        break
    string_buffer.append(c * l)
else:
    print("".join(string_buffer))
