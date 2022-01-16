n, s = map(int, input().split())
A = list(map(int, input().split()))
dp = [0] * (s + 1)
dp[0] = 1
for a in A:
    for i in reversed(range(s + 1)):
        if i + a <= s:
            dp[i + a] |= dp[i]
print('Yes' if dp[s] else 'No')