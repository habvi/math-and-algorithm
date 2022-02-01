n = int(input())
A = list(map(int, input().split()))

dp = [0] * n
dp[:2] = A[:2]

for i in range(2, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + A[i])
    
print(dp[-1])