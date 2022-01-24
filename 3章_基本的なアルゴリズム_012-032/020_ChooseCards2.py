n = int(input())
A = list(map(int, input().split()))
K = 5
m = 1000

dp = [[0] * (m + 1) for _ in range(K + 1)]
dp[0][0] = 1
for a in A:
    for i in reversed(range(K)):
        for j in reversed(range(m + 1)):
            if j + a <= m:
                dp[i + 1][j + a] += dp[i][j]
print(dp[K][m])