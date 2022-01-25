n = int(input())
B = list(map(int, input().split()))
R = list(map(int, input().split()))

sr = sum(R)
tot = 0
for b in B:
    tot += b * n + sr
print(1 / n**2 * tot)