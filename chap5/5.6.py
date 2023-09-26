"""
Wを実現できるか（各itemに回数制限蟻）
"""
if __name__ =='__main__':
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    M = list(map(int, input().split())) 
    dp = [[False]*(W+1) for i in range(N+1)]
    
    for i in range(N+1):
        dp[i][0] = True
    
    for i in range(1, N+1):
        for w in range(1, W+1):
            if w - A[i-1] >= 0:  # A[i-1] なのはdpのインデックスと合わせるため
                # 回数制限の判定. 
                if w - A[i-1] in [A[i-1] * m for m in range(M[i-1])]:
                    dp[i][w] = any([dp[i-1][w - A[i-1]], dp[i][w - A[i-1]], dp[i-1][w]])
                else:
                    dp[i][w] = any([dp[i-1][w - A[i-1]], dp[i-1][w]])
                    
            else:
                dp[i][w] = dp[i-1][w]
    print(dp[-1][-1])