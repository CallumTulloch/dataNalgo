"""
値を必要なおもりの最小個数で更新する．
INFを初期値にするのがポイント
"""
INF = float('inf')

if __name__ =='__main__':
    N, W, K = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [[INF]*(W+1) for i in range(N+1)]

    for i in range(N+1):
        dp[i][0] = 0
    
    for i in range(1, N+1):
        for w in range(1, W+1):
            if w - A[i-1] >= 0:  # A[i-1] なのはdpのインデックスと合わせるため
                dp[i][w] = min(dp[i-1][w - A[i-1]] + 1, dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    # k以下で実現できるか
    print(True if dp[-1][-1] <= K else False)
    for a in dp:
        print(a)