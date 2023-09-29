"""
貪欲の場合，正しく解くことができない
"""
# N = int(input())
# A = list(map(int, input().split()))
# 
# summ = 0
# while len(A) != 1:
#     sum_of_aja = []
#     for i in range(len(A)-1):
#         sum_of_aja.append(A[i] + A[i+1])
#     index_of_min = min(enumerate(sum_of_aja), key=lambda x: x[1])[0]
#     value = A[index_of_min] + A[index_of_min + 1]
#     A.pop(index_of_min + 1)  # 先に+1側をpopする
#     A.pop(index_of_min)
#     A.insert(index_of_min, value)
#     summ += value
# 
# print(summ)

"""
DP 
i と j は区間をイメージすること．0番目にスライムは存在しないとする．
Reの方が，直感的でわかりやすい．
"""
N = int(input())
A = list(map(int,input().split()))
INF = float('inf')

# スライムの大きさの累積和を計算．
# 毎回計算するのは効率が悪い．
acc=[0]
for a in A:
    acc.append(acc[-1] + a)

# i番目からj番目までのスライムを合体させるための最小コストを保持します。
dp = [[INF]*(N+1) for _ in range(N+1)]
for i in range(N):
    dp[i][i+1] = 0

# i, k, j をどう選ぶか → i, k, j の間が最小になるものから見ていく＝DPの基本．betはiとの差分（最小で2）
for bet in range(2, N+1):
    for i in range(N):
        j = i + bet
        if j > N:
            continue
        # 更新
        for k in range(i+1,j):                                              # dp[i][j] はi, j まででスライムを1体にするためのコスト
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + acc[j] - acc[i]) # i~kまでのコスト ＋ k~j までのコスト ＋ acc[j]-acc[i]（この2つを足すコスト）

print(dp[0][N])


"""
DP(もっと効率がよいもの)
"""
#from itertools import*
#n=int(input())
#A=list(map(int,input().split()))
## dp[l][r]:区間[l,r]に相当するスライムが1匹にまとまっている時それを分解するための必要な最小コスト
#ACC=[0]+list(accumulate(A))
#INF=10**20
#dp=[[0]*n for _ in range(n)]
#C=[[0]*n for _ in range(n)]
#for i in range(1,n):
#    C[i][i]=i-1
#for j in range(1,n):
#    for i in range(n-j):
#        l=i
#        r=i+j
#        tmp=INF
#        for k in range(C[i][i+j-1],C[i+1][i+j]+1):
#            t=dp[l][k]+dp[k+1][r]
#            if t<=tmp:
#                tmp=t
#                C[l][r]=k
#        dp[i][i+j]=ACC[r+1]-ACC[l]+tmp
#print(dp[0][-1])

"""
2分探索 提出 #23497362
"""
#from heapq import heappop, heappush, heapify
# 
#class Heap():
#    def __init__(self, val):
#        self.val = val
#        self.lt = None
#        self.rt = None
# 
#def meld(a, b):
#    if a is None: return b
#    if b is None: return a
#    if a.val > b.val: a, b = b, a
#    a.rt = meld(a.rt, b)
#    a.lt, a.rt = a.rt, a.lt
#    return a
# 
#def top(a):
#    return a.val
# 
#def pop(a):
#    return meld(a.lt, a.rt)
# 
#def push(a, x):
#    b = Heap(x)
#    return meld(a, b)
# 
#INF = (1 << 60) - 1
# 
#def hu_tucker(n, arr):
#    w = list(arr)
#    lt = [0] * n
#    rt = [0] * n
#    cost = [0] * (n - 1)
#    heap = [None for _ in range(n - 1)]
#    queue = []
#    for i in range(n - 1):
#        lt[i] = i - 1
#        rt[i] = i + 1
#        cost[i] = w[i] + w[i + 1]
#        queue.append(cost[i] * n + i)
#    heapify(queue)
#    res = 0
#    for _ in range(n - 1):
#        while True:
#            p = heappop(queue)
#            c, i = divmod(p, n)
#            if cost[i] == c and rt[i] >= 0: break
#        ml = mr = False
#        if heap[i] is not None and w[i] + heap[i].val == c:
#            heap[i] = pop(heap[i])
#            ml = True
#        elif w[i] + w[rt[i]] == c:
#            ml = mr = True
#        else:
#            t = top(heap[i])
#            heap[i] = pop(heap[i])
#            if heap[i] is not None and top(heap[i]) + t == c:
#                heap[i] = pop(heap[i])
#            else:
#                mr = True
#        res += c
#        heap[i] = push(heap[i], c)
#        if ml: w[i] = INF
#        if mr: w[rt[i]] = INF
#        if ml and i > 0:
#            j = lt[i]
#            heap[j] = meld(heap[i], heap[j])
#            rt[j] = rt[i]
#            rt[i] = -1
#            lt[rt[j]] = j
#            i = j
#        if mr and rt[i] + 1 < n:
#            j = rt[i]
#            heap[i] = meld(heap[i], heap[j])
#            rt[i] = rt[j]
#            rt[j] = -1
#            lt[rt[i]] = i
#        cost[i] = w[i] + w[rt[i]]
#        if heap[i] is not None:
#            t = top(heap[i])
#            heap[i] = pop(heap[i])
#            cost[i] = min(cost[i], w[i] + t, w[rt[i]] + t)
#            if heap[i] is not None: cost[i] = min(cost[i], top(heap[i]) + t)
#            heap[i] = push(heap[i], t)
#        heappush(queue, cost[i] * n + i)
#    return res
# 
#import sys
#input = sys.stdin.buffer.readline
# 
#print(hu_tucker(int(input()), map(int, input().split())))