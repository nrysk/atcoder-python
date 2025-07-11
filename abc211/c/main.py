char_to_index = {char: i for i, char in enumerate("chokudai")}
dp = [0 for _ in range(len("_chokudai"))]
dp[0] = 1

s = input()

for char in s:
    if char in char_to_index:
        index = char_to_index[char]
        dp[index + 1] += dp[index]
print(dp[-1] % (10**9 + 7))
