t = int(input())
ans = []


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    # 全ての絶対値が等しい場合
    if all(abs(x) == abs(a[0]) for x in a):
        # 全て正または全て負の場合
        if all(x >= 0 for x in a) or all(x <= 0 for x in a):
            ans.append("Yes")
            return
        else:
            count_pos = sum(1 for x in a if x > 0)
            count_neg = sum(1 for x in a if x < 0)
            # 正の数と負の数の差が1以下の場合
            if abs(count_pos - count_neg) <= 1:
                ans.append("Yes")
                return
            else:
                ans.append("No")
                return

    b = sorted(a, key=abs)
    # b が等比数列か
    if n == 1 or n == 2:
        ans.append("Yes")
        return
    for i in range(2, n):
        if b[i - 1] * b[1] != b[i] * b[0]:
            ans.append("No")
            return

    ans.append("Yes")
    return


for _ in range(t):
    solve()
print("\n".join(ans))
