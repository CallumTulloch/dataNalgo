import itertools
N, M = map(int, input().split())
P = [int(input()) for _ in range(N)]

S = []
for i, j in itertools.combinations_with_replacement(P):
        S.append(i + j)

S.sort()
for s in S:
    
    