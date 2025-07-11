class Node:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None


t = int(input())


def dfs(node, result):
    if node.left is None and node.right is None:
        result.append(node.value)
        return
    dfs(node.left, result)
    dfs(node.right, result)


def solve():
    n = int(input())
    p = list(map(int, input().split()))

    # 完全二分木の構築
    nodes = [Node() for _ in range(2 ** (n + 1) - 1)]
    # 葉ノード
    for i in range(2**n):
        nodes[i + 2**n - 1].value = p[i]
    # 内部ノードは子要素の最小値
    for i in reversed(range(2**n - 1)):
        left = nodes[2 * i + 1]
        right = nodes[2 * i + 2]
        nodes[i].value = min(left.value, right.value)
        nodes[i].left = left
        nodes[i].right = right

    # 値から順番に値が小さい方を左にする
    for i in range(2**n - 1):
        if nodes[i].left and nodes[i].right:
            if nodes[i].left.value > nodes[i].right.value:
                nodes[i].left, nodes[i].right = nodes[i].right, nodes[i].left

    # 左の葉ノードから順に値を出力
    result = []
    dfs(nodes[0], result)
    print(" ".join(map(str, result)))


for _ in range(t):
    solve()
