# n, x = map(int, input().split())
# A = set(map(int, input().split()))
# print('Yes' if x in A else 'No')



def binary_search(left, right):
    if right - left == 1:
        return A[left] == x
    
    mid = (left + right) // 2
    return binary_search(left, mid) or binary_search(mid, right)


n, x = map(int, input().split())
A = list(map(int, input().split()))

print('Yes' if binary_search(0, n) else 'No')