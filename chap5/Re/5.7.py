S = input()
T = input()
MINF = float('inf') * -1

dp = [[0] * (len(T)+1) for _ in range((len(S)+1))]
# init dp
#dp[0] = list([0] * (str_len+1))
#for i in range(str_len+1):
#    dp[i][0] = 0

for i in range(1, len(S)+1):
    for j in range(1, len(T)+1):
        if S[i-1] == T[j-1]:    # dpと合わせるために+1している．
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# decode
i, j = len(S), len(T)
result = []
while i > 0 and j > 0:
    #print(i,j)
    if S[i-1] == T[j-1]:
        result.append(S[i-1])
        i -= 1
        j -= 1
    elif dp[i-1][j] > dp[i][j-1]:   # 上の方がでかい
        i -= 1
    else:
        j -= 1
#print(dp)
print(''.join(result[::-1]))