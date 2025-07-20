t = int(input())


def rec(state, visited, n, s):
    # print(state, visited, n, s)
    state_num = int(state, 2)
    if visited[state_num]:
        return False
    visited[state_num] = True
    if s[state_num - 1] == "1":
        return False
    if state_num == 0:
        return True

    # 1を一つ消す
    for i in range(n):
        if state[i] == "1":
            next_state = state[:i] + "0" + state[i + 1 :]
            if rec(next_state, visited, n, s):
                return True
    return False


def solve():
    n = int(input())
    s = input()

    # bit全探索を使う
    visited = [False] * (2**n)

    if rec("1" * n, visited, n, s):
        print("Yes")
    else:
        print("No")


for _ in range(t):
    solve()
