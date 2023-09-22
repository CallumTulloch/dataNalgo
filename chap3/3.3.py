def main():
    # 入力受け取り
    N = int(input())
    a = [int(x) for x in input().split()]
    # 初期化として無限大
    minv = float('inf')
    second_minv = float('inf')
    for i in range(N):
        # 最小値を見つけた場合
        if a[i] < minv:
            # minvを2番目に
            second_minv = minv
            # 探索した値をminvに
            minv = a[i]
        # 2番目に小さい値を見つけた場合
        elif a[i] < second_minv:
            second_minv = a[i]
    print(second_minv)
if __name__ == '__main__':
    main()
    
    
"""被ってはならない場合
A = list(map(int, input().split()))

mini = A[0]
mini2 = A[1]
for a in A:
    if a < mini:
        mini2 = mini
        mini = a
print(mini, mini2)
"""