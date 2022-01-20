from functools import reduce
from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

n = int(input())
a = list(map(int, input().split()))
print(reduce(lcm, a))