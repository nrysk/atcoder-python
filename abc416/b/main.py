s = input().strip()

flg = True
string_buffer = []

for i in range(len(s)):
    if s[i] == "." and flg:
        string_buffer.append("o")
        flg = False
    elif s[i] == "#":
        flg = True
        string_buffer.append("#")
    else:
        string_buffer.append(".")

print("".join(string_buffer))
