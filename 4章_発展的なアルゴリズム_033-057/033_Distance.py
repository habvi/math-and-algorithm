def dst_line_to_point(x1, y1, x2, y2, px, py):
    nmrt = abs((y2 - y1)*px + (x1 - x2)*py + x2*y1 - y2*x1)
    dnmnt = ((y2 - y1)**2 + (x2 - x1)**2) ** 0.5
    return nmrt / dnmnt

def dst_two_points(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5


ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())

A = cy - by
B = bx - cx
C = by*cx - bx*cy

lx = (B*(B*ax - A*ay) - A*C) / (A**2 + B**2)
ly = (A*(-B*ax + A*ay) - B*C) / (A**2 + B**2)

if min(bx, cx) <= lx <= max(bx, cx) and min(by, cy) <= ly <= max(by, cy):
    print(dst_line_to_point(bx, by, cx, cy, ax, ay))
else:
    print(min(dst_two_points(ax, ay, bx, by), dst_two_points(ax, ay, cx, cy)))