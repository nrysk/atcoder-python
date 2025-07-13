import itertools

a = int(input())
n = int(input())

digits = [str(i) for i in range(a)]


def is_palindrome(s):
    return s == s[::-1]


sum = 0
i = 0
while True:
    for p in itertools.product(digits, repeat=i // 2 + 1):
        s = "".join(p)
        if s[0] == "0":
            continue
        # s を反転させて連結し回文にする
        if i % 2 == 0:
            s = s[:-1] + s[::-1]
        else:
            s = s + s[::-1]
        # s を10進数に変換
        num = int(s, a)
        if num == 0:
            continue
        if num > n:
            print(sum)
            exit()
        elif is_palindrome(str(num)):
            # print(s, num)
            sum += num
    i += 1
print(sum)
