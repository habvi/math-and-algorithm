def dist_two_points(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5


x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

dist = dist_two_points(x1, y1, x2, y2)
rs = r1 + r2

if rs < dist:
    print(5)
elif rs == dist:
    print(4)
elif max(r1, r2) - min(r1, r2) < dist:
    print(3)
elif max(r1, r2) - min(r1, r2) == dist:
    print(2)
else:
    print(1)