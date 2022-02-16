from math import cos, radians

def law_of_cos(a, b, angle):
    return (a**2 + b**2 - 2*a*b*cos(radians(angle))) ** 0.5


a, b, H, M = map(int, input().split())

h = 360 // 12 * H + 360 / 12 / 60 * M
m = 360 // 60 * M

print(law_of_cos(a, b, abs(h - m)))