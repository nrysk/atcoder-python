import itertools

class ModCombinations:
    def __init__(self, max_n, mod):
        self.max_n = max_n
        self.mod = mod
        
        self.fact = [1] * (max_n + 1)
        self.inv_fact = [1] * (max_n + 1)
        
        for i in range(1, max_n + 1):
            self.fact[i] = (self.fact[i-1] * i) % self.mod
        
        self.inv_fact[max_n] = pow(self.fact[max_n], self.mod - 2, self.mod)

        for i in range(max_n, 0, -1):
            self.inv_fact[i-1] = (self.inv_fact[i] * i) % self.mod

    def nCr(self, n, r):
        """
        組み合わせ nCr (mod p) を O(1) で計算
        """
        if r < 0 or r > n:
            return 0
        # n! * (r!)⁻¹ * ((n-r)!)⁻¹
        numerator = self.fact[n]
        denominator = (self.inv_fact[r] * self.inv_fact[n-r]) % self.mod
        return (numerator * denominator) % self.mod

    def nPr(self, n, r):
        """
        順列 nPr (mod p) を O(1) で計算
        """
        if r < 0 or r > n:
            return 0
        # n! * ((n-r)!)⁻¹
        numerator = self.fact[n]
        denominator = self.inv_fact[n-r]
        return (numerator * denominator) % self.mod

mod_combinations = ModCombinations(100,  998244353)

n, l = map(int, input().split())
s = []
for _ in range(n):
    s.append(input().strip())


def calc_overlap(s1, s2):
    ret = []
    length = min(len(s1), len(s2))
    for i in range(1, length + 1):
        if s1[-i:] == s2[:i]:
            ret.append(i)
    return ret


overlap_dict = {
    (i, j): calc_overlap(s[i], s[j]) for i in range(n) for j in range(n) if i != j
}

# オーバーラップする場合としない場合で，文字列の塊の数が異なる
for indices in itertools.permutations(range(n)):
    for i, index in enumerate(indices):
        for overlap in overlap_dict[(index, indices[i + 1])]:
