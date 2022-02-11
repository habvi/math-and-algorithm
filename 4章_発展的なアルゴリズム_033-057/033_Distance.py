def dist_line_to_point(x1, y1, x2, y2, px, py):
    nmrt = abs((y2 - y1)*px + (x1 - x2)*py + x2*y1 - y2*x1)
    dnmnt = ((y2 - y1)**2 + (x2 - x1)**2) ** 0.5
    return nmrt / dnmnt

def dist_two_points(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

def equation_of_the_line(x1, y1, x2, y2):
    if x1 == x2:
        return 1, 0, -x1
    A = y2 - y1
    B = x1 - x2
    C = y1*x2 - x1*y2
    return A, B, C

def point_closest_to_the_line(A, B, C, x, y):
    lx = (B*(B*x - A*y) - A*C) / (A**2 + B**2)
    ly = (A*(-B*x + A*y) - B*C) / (A**2 + B**2)
    return lx, ly


ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())

A, B, C = equation_of_the_line(bx, by, cx, cy)
lx, ly = point_closest_to_the_line(A, B, C, ax, ay)

if min(bx, cx) <= lx <= max(bx, cx) and min(by, cy) <= ly <= max(by, cy):
    print(dist_line_to_point(bx, by, cx, cy, ax, ay))
    # same
    # print(dist_two_points(lx, ly, ax, ay))
else:
    print(min(dist_two_points(ax, ay, bx, by), dist_two_points(ax, ay, cx, cy)))