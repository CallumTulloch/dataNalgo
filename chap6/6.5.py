"""
問題の言い換え：(K番目に小さい値を求めなさい」という問題に対しては二分探索法が有効)
N2個の整数のうち、x以下の値が K個以上あるかどうかを判定せよ．

アルゴリズム：
最小=0, 最大=a[-1]*b[-1] のなかから，xを見つける．
aを固定し，そのaの値でb全体をわり，2分探索でx以下になるものの数を見つける．
見つかった数がkの物が，求めるxの答えとなる．
"""

import bisect

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
K = int(input(()))
aA = sorted(A)
aB = sorted(B)

right = N
left = 0
mid = int(N/2)
while (mid)**2 <= K <= (mid+1)**2:
    mid = int(()/2)


left = K - mid**2
