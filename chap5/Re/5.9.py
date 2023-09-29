import itertools

N = int(input())
A = list(map(int, input().split()))
INF = float('inf')

# 累積和の計算
A = [0] + A
acc = list(itertools.accumulate(A))

# dp[i][j] はiからj番目までのスライムを合体させるための最小コスト
dp = [[INF] * (N+1) for _ in range(N+1)]
for i in range(N):
    dp[i][i] = 0    # スライム単体は合体させる必要がない．

# DPの更新
for bet in range(1, N):  # betは区間の長さの差分
    for i in range(N - bet):
        j = i + bet
        for k in range(i, j):  
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + acc[j+1] - acc[i])
            # dp[0][0] + dp[1][1] + acc 

print(dp[0][N-1])
