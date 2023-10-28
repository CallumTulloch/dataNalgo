"""
問題の言い換え：(K番目に小さい値を求めなさい」という問題に対しては二分探索法が有効)
N2個の整数のうち、x以下の値が K個以上あるかどうかを判定せよ．

アルゴリズム：
最小=0, 最大=a[-1]*b[-1] のなかから，xを見つける．
aを固定し，そのaの値でb全体をわり，2分探索でx以下になるものの数を見つける．
見つかった数がkの物が，求めるxの答えとなる．

memo
l = mid とするのは，lが必ずno, rが必ずyesになるというような状況の場合で，継続条件はright-left>1
層でない場合は，mid-1 and mid+1で，条件はｋ，right>left である．
"""

import bisect

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
K = int(input(()))
sA = sorted(A)
sB = sorted(B)

l = 0
r = max(sA[-1], sB[-1])
cnt = 0
while r > l:
    mid = int((r + l)/2)
    for a in A:
        idx = bisect.bisect(mid, [b / a for b in B])
        cnt += idx
    if K == cnt:
        print()
        break
    elif K > cnt:
        l = mid + 1 
    else:
        r = mid - 1
    cnt = 0

print(mid)