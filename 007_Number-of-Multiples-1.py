n, x, y = map(int, input().split())
print(sum([1 for i in range(1, n + 1) if i % x == 0 or i % y == 0]))