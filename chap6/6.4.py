"""
最大値の最小化と最小値の最大化に関する最適化は同じアプローチをとる．
つまり，N 個の小屋から M 個を選ぶ。このとき、どの 2 つの小屋の間隔も x 以上離れている状態にすることは可能か？
point : 最初の部屋は絶対選ばれ，貪欲法をもちいる．
point : 更新の際は+1を忘れずに
"""
import bisect

def is_valid(A, M, gap):
    """指定のM間隔で区切れるか？
    Args:
    A : 家の座標
    M : 選ぶ家の数 → cnt は+1とする．
    g : 最小の間隔
    
    return: bool
    """
    l = A[0]
    cnt = 1
    print('gap : ', gap)
    for a in A[1:]:
        dist = abs(a - l)
        print(a, '-',  l, dist>=gap)
        if dist >= gap:
            cnt += 1
            l = a
        if cnt == M:
            return True
    return False


N, M = map(int, input().split())
A = list(map(int, input().split()))
A = sorted(A)
print(A)

l = 0
r = A[-1] - A[0]
maxi = 0
while r >= l:
    mid = int((r + l) / 2)
    print(r,l,mid)
    if is_valid(A, M, mid):
        maxi = mid
        l = mid + 1
    else:
        r = mid - 1

print(maxi)

# 5 3
# 1 2 8 4 9