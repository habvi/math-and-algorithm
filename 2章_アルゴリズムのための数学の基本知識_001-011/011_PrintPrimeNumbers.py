def primes(mx):
    pr = list(range(3, mx + 1, 2))
    ln = len(pr)
    for i, k in enumerate(pr):
        if k:
            if k * k > mx:
                break
            for j in range(i + k, ln, k):
                pr[j] = 0
    yield 2
    yield from [p for p in pr if p]

n = int(input())
print(*primes(n))