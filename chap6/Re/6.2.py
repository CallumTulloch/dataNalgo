import bisect

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
sA = sorted(A)
sB = sorted(B)
sC = sorted(C)

cnt = 0
for b in sB:
    num_a = bisect.bisect_left(b, sA)
    num_c = len(C) - bisect(b, sC)
    cnt += num_a * num_c
print(cnt)