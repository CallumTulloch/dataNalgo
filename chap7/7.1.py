"""
前から見ていく，からO(NlogN + N) = O(NlogN)になる．
二分探索の場合，O(NlogN + NlogN)
"""
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
#' '.join(map(str,list(np.random.randint(100,size=10))))
sA = sorted(A)
sB = sorted(B)

I = 0
cnt = 0
for a in sA:
    for i in range(I, N):
        if a < sB[i]:
            cnt += N - i
            I = i
            break
    else:
        I = i

print(cnt)