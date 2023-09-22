"""
  0 1 2 3
a 0 3
b 0 3
c 0 4 

a -> b or c, b -> a or c 的な遷移
"""

if __name__ == '__main__':
    N = int(input())
    dp = [[-1]*(3) for i in range(N+1)]
    
    a, b, c = map(int, input().split())
    dp[0] = [0, 0, 0]
    dp[1] = [a, b, c] 
    
    # 2日以降
    for i in range(2, N+1):
        a, b, c = map(int, input().split())
        # a への遷移
        dp[i][0] = a + max(dp[i-1][1], dp[i-1][2])
        # b への遷移
        dp[i][1] = b + max(dp[i-1][0], dp[i-1][2])
        # c への遷移
        dp[i][2] = c + max(dp[i-1][0], dp[i-1][1])
    
    print(max(dp[:][-1]))
        
        