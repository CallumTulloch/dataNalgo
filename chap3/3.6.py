# X, Y が決まれば　Z は自動的に決まる方針
if __name__ == '__main__':
    # 0 <= X, Y, Z <= K, X + Y + Z = N
    K, N = map(int, input().split())
    count = 0
    for i in range(N+1):
        for j in range(0, K, 1):
            Y = N - i - j
            if Y >= 0:
                count += 1
    print(count)