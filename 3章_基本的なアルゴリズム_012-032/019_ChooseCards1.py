from collections import Counter

def nC2(n):
    return n * (n - 1) // 2

n = int(input())
A = list(map(int, input().split()))

ans = 0
for _, v in Counter(A).items():
    if v >= 2:
        ans += nC2(v)
print(ans)