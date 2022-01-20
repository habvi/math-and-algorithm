from collections import Counter
n = int(input())
a = list(map(int, input().split()))

c = Counter(a)
print(c[100] * c[400] + c[200] * c[300])