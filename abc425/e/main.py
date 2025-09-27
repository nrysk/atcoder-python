import sys
from collections import defaultdict

input = sys.stdin.readline


class ModUtil:
    def __init__(self, max_n, mod):
        self.max_n = max_n
        self.mod = mod

        self._factorial_factors_table = [defaultdict(int) for _ in range(max_n + 1)]

        self._precompute_factorial_factors()

    def _precompute_factorial_factors(self):
        # エラトステネスのふるいを応用して高速化
        factors_of_n = [defaultdict(int) for _ in range(self.max_n + 1)]
        for i in range(2, self.max_n + 1):
            if not factors_of_n[i]:  # iが素数の場合
                for j in range(i, self.max_n + 1, i):
                    num = j
                    while num % i == 0:
                        factors_of_n[j][i] += 1
                        num //= i

        # 累積和の考え方で k! = (k-1)! * k を計算
        for k in range(1, self.max_n + 1):
            # (k-1)! の素因数分解をコピー
            current_factors = self._factorial_factors_table[k - 1].copy()
            # k の素因数分解を加算
            for prime, exponent in factors_of_n[k].items():
                current_factors[prime] += exponent
            self._factorial_factors_table[k] = current_factors

    def _get_factorial_prime_factorization(self, n):
        if not 0 <= n <= self.max_n:
            raise ValueError("n is out of pre-computation range")
        return self._factorial_factors_table[n].copy()

    def permutations_with_repetition(self, counts):
        n = sum(counts)
        if n > self.max_n:
            raise ValueError("n is too large")

        # 分子の素因数分解をテーブルから取得
        final_factors = self._get_factorial_prime_factorization(n)

        # 分母の素因数分解を引く
        for count in counts:
            if count > 1:
                denom_factors = self._get_factorial_prime_factorization(count)
                for p, exp in denom_factors.items():
                    final_factors[p] -= exp

        # 結果を組み立てる
        result = 1
        for p, exp in final_factors.items():
            if exp > 0:
                result = (result * pow(p, exp, self.mod)) % self.mod

        return result


t, m = map(int, input().split())

mod_util = ModUtil(5000, m)

for _ in range(t):
    n = int(input())
    c = list(map(int, input().split()))
    print(mod_util.permutations_with_repetition(c))
