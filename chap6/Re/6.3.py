import itertools
import bisect

N, M = map(int, input().split())
#P = list(map(int, input().split()))
P = [int(input()) for _ in range(N)] 

S = []
for i, j in itertools.combinations_with_replacement(P, 2):
        S.append(i + j)

S.sort()
maxi = 0
for s in S:
    idx = bisect.bisect_right(S, M-s)
    if idx == 0:
            continue
    maxi = max(maxi, s+S[idx-1])

print(maxi)