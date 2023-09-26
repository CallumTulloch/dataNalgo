#import itertools
#
#N, K = map(int, input().split())
#K -= 1 # 区切りで考える．
#A = list(map(int, input().split()))
#Acc = list(itertools.accumulate(A))
#C = [[-1]*N for _ in range(N)]
#
## wakati 同様，区間のスコアを計算する．区間は j ~ i = [j][i]とする．
#for i in range(N):
#    for j in range(i):
#        C[j][i] = (Acc[i] - Acc[j]) / (i - j + 1)
#
## ある地点 i における k 区切りでの最大を更新していく．j は i 番目で最大を見つける際に，それまでの番地での最大値として使用．
#dp = [[-1]*K for _ in range(N)]
#for i in range(N):
#    dp[i][0] = Acc[i] / (i+1)
#
#print(dp)
#for i in range(0, N):
#    for j in range(i):  # iまでの最適はすでに求まっている．
#        for k in range(1, K):
#            dp[i][k] = max(dp[i][k], dp[j][k-1] + C[j][i])
#
#print(dp)
#print(dp[-1][K-1])

"""
区間DPは0番目は存在しない = 値は0として置くこと．
"""

def max_average_partition(N, M, A):
    # 区間 [j, i) の平均値を前処理で求める
    f = [[0]*(N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(i):
            f[j][i] = sum(A[j:i]) / (i - j)

    # DP
    dp = [[-float('inf')]*(M+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(1, N+1):
        for j in range(i):
            for k in range(1, M+1):
                dp[i][k] = max(dp[i][k], dp[j][k-1] + f[j][i])
    print(dp)
    # 最終結果を計算
    return max(dp[N])

N, M = map(int, input().split())
A = list(map(int, input().split()))
print(max_average_partition(N, M, A))