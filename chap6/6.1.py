import bisect

A = list(map(int, input().splti()))
sA = sorted(A)

for a in A:
    print(bisect.bisect(sA, a), end=' ')