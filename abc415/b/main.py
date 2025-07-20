s = input()


# '#' を2つ見つけるごとに添え字を出力
flg = False
for i in range(len(s)):
    if s[i] == "#":
        if flg:
            print(i + 1)
            flg = False
        else:
            print(f"{i + 1},", end="")
            flg = True
