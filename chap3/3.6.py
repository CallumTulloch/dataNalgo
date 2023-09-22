"""
1. 0≦X,Y,Z≦K の意味を取り違えないこと．
2. X, Y が決まればZ は自動的に決まる方針
"""

if __name__ == '__main__':
    # 0 <= X, Y, Z <= K, X + Y + Z = N
    K, N = map(int, input().split())
    count = 0
    for x in range(0, K+1, 1):
        for z in range(0, K+1, 1):
            Y = N - x - z
            if K >= Y >= 0:
                count += 1
                #print(x, Y, z)
    print(count)