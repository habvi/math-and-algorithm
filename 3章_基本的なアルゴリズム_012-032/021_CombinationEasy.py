from math import factorial
def P(n, r):
    return factorial(n) // factorial(n - r)

def C(n,r):
    return P(n, r) // factorial(r)

n, r = map(int, input().split())
print(C(n, r))