import collections

A = list(map(int, input().split()))
c = collections.Counter(A)
print(c[3])