# n, x = map(int, input().split())
# A = set(map(int, input().split()))
# print('Yes' if x in A else 'No')


def is_ok(i):
    return A[i] <= x

def bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid


n, x = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

i = bisect(n, 0)
print('Yes' if A[i] == x else 'No')