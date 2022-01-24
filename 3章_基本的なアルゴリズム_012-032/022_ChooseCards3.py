from collections import Counter

n = int(input())
A = list(map(int, input().split()))
c = Counter(A)

m = 100000
ans = 0
for a in A:
    c[a] -= 1
    ans += c[m - a]    
print(ans)