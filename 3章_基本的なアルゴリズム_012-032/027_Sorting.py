# n = int(input())
# print(*sorted(map(int, input().split())))



from collections import deque

class MergeSort:
    def __init__(self, A, left, right):
        self.A = A
        self.left = left
        self.right = right
    
    def mergesort(self):
        return self.split_half(self.left, self.right)
        
    def split_half(self, left, right):
        if left + 1 < right:
            mid = (left + right)//2
            self.split_half(left, mid)
            self.split_half(mid, right)
            self.merge(self.A, left, mid, right)
            return self.A
        
    def merge(self, A, left, mid, right):
        L = deque(A[left : mid])
        R = deque(A[mid : right])
        for i in range(left, right):
            if not L:
                self.A[i] = R.popleft()
            elif not R:
                self.A[i] = L.popleft()
            elif L[0] <= R[0]:
                self.A[i] = L.popleft()            
            else:
                self.A[i] = R.popleft()
            

n = int(input())
A = list(map(int, input().split()))
ms = MergeSort(A, 0, n)
print(*ms.mergesort())