def lcs(s, t):
    # dp[i][j] は s の最初の i 文字と t の最初の j 文字の最長共通部分列の長さを表す
    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])  # 最長だからmax

    # 最長共通部分列を復元（大きいほうに流れていく）
    i, j = len(s), len(t)
    result = []
    while i > 0 and j > 0:
        if s[i-1] == t[j-1]:
            result.append(s[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:   # 上の方がでかい
            i -= 1
        else:
            j -= 1

    return ''.join(result[::-1])

# 入力
s = input().strip()
t = input().strip()

# 出力
print(lcs(s, t))
