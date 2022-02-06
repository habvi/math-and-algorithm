def dist_two_points(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5


n = int(input())
xy = [tuple(map(int, input().split())) for _ in range(n)]

ans = float('inf')
for i, (x, y) in enumerate(xy):
    for j in range(i + 1, n):
        ans = min(ans, dist_two_points(x, y, xy[j][0], xy[j][1]))
print(ans)