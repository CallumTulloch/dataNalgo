

if __name__ =='__main__':
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [[False]*(W+1) for i in range(N+1)]
    
    for i in range(N+1):
        dp[i][0] = True
    
    for i in range(1, N+1):
        for w in range(1, W+1):
            if w - A[i-1] >= 0:  # A[i-1] なのはdpのインデックスと合わせるため
                dp[i][w] = any([dp[i-1][w - A[i-1]], dp[i-1][w]])
            else:
                dp[i][w] = dp[i-1][w]
    print(dp[-1][-1])