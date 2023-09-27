import bisect
import collections

A = list(map(int, input().split()))
sA = sorted(A)
c = collections.Counter
max_val = max(c(sA).values)
print(sA)

for a in A:
    if max_val == 1: # 一意
        print(bisect.bisect(sA, a), end=' ')
    else: # 任意
        print(bisect.bisect_left(sA, a), end=' ')