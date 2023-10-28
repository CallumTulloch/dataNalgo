"""
Wを実現できるか（各itemに回数制限蟻）
同ステップ内での遷移は不可能．その代わり，M[i-1]回（最大使用可能回数）までの繰り返し内で、w - k * A[i-1]における前のDPテーブルの値を参照しています。
つまり，前のステップで複数のおもりの位置を基に更新するということ．
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
            dp[i][w] = dp[i-1][w]
            for k in range(1, M[i-1] + 1):  # 各おもりに対して、使用可能な回数だけ繰り返す
                if w - k * A[i-1] >= 0:
                    dp[i][w] |= dp[i-1][w - k * A[i-1]]
                else:
                    break  # これ以上の重さを考慮することはできないので、ループを抜ける
    
    print(dp[-1][-1])