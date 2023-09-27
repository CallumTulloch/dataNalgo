import bisect

"""
A固定だとN**2logNTLE. B固定だとNlogN
bisect は同じ値の場合一番右側で挿入すべきヶ所を教えてくれる．
"""

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
sA = sorted(A)
sB = sorted(B)
sC = sorted(C)

cnt = 0
for b in sB:
    a_num = bisect.bisect_left(sA, b)
    c_num = len(C) - bisect.bisect(sC, b)
    cnt += a_num * c_num
print(cnt)