"""[i, j]で考える
区間DPの[j, i)で考えるメリットが良くわからない．
[i, j]の方が直感的．注意点として，0 は何もないこと．また，loopの際には j を決めてから各iを動かす事に注意．
"""
import itertools

N, M = map(int, (input().split()))
A = list(map(int, input().split()))
A = [0] + A
INF = float('inf')*-1

Acc = list(itertools.accumulate(A))
S = [[INF]*(N+1) for _ in range(N+1)]
print(Acc)
for i, j in itertools.combinations(range(N+1), 2):
    S[i][j] = (Acc[j] - Acc[i]) / (j-i)
for i in range(N+1):
    S[i][i] = A[i]

# dp[j][k] : k区切りにおける，j番目までの最適値
dp = [[INF]*(M+1) for k in range(N+1)]
dp[0] = [0]*(N+1)
for j in range(N+1):
    for i in range(j):
        for k in range(1, M+1):   # 区間は最小で1つから
            if j >= k:
                dp[j][k] = max(dp[j][k], dp[i][k-1] + S[i][j]) # -inf + someting であれば，右が選ばれる．

print(dp)
print(dp[-1][M])