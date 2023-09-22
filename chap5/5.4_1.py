# このプログラムは採用のおもりを

if __name__ =='__main__':
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [[0]*(W+1) for i in range(N+1)]
    
    for i in range(N+1):
        dp[i][0] = 1
    
    for i in range(1, N+1):
        for w in range(1, W+1):
            dp[i][w] = dp[i-1][w]
            if dp[i][w] == False and w - A[i-1] >= 0:  # A[i-1] なのはdpのインデックスと合わせるため
                dp[i][w] = dp[i-1][w - A[i-1]] + 1
    # 1以上W未満の重みのそれぞれについて，　実現可能数を足し算する．
    print(dp[-1])
    print(sum(dp[-1][1:W]))
    print(sum(dp[-1]))