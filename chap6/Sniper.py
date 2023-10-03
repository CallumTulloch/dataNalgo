"""
本来，秒数に指定は存在しないが最大の高度を決めて，それに達するかどうかを判断するという方法.
今回のアルゴリズムは、mid を可能な高さとしてセットし、各風船がその高さ以下で爆発するかどうかを確認することで、最も低い高さを求めることができる．
"""

def solve_balloons(N, HS):
    M = 0   # 最大高度
    # 最悪の場合、風船は1つずつ順番に爆発するため、最後の風船が爆発するまでには N 秒かかる
    for h, s in HS:
        M = max(M, h + s * N)

    left, right = 0, M
    while right - left > 1:
        mid = (left + right) // 2
        
        ok = True
        t = [0] * N
        for i in range(N):
            h, s = HS[i]
            # 開始の段階で満たしていない → false （条件分岐をもっとうまく活用すればもうちょっとだけ早くなる．）
            if mid < h:
                ok = False
            else:
                t[i] = (mid - h) // s
        
        # それぞれ，割らなければならない時間があり，毎秒毎にそれが満たされているか確認する．
        t.sort()
        for i in range(N):
            if t[i] < i:
                ok = False
        
        if ok:
            right = mid
        else:
            left = mid
    
    return right

# Input
N = int(input())
HS = [tuple(map(int, input().split())) for _ in range(N)]

# Solve and print the result
print(solve_balloons(N, HS))
