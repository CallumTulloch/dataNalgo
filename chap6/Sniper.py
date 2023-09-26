def solve_balloons(N, HS):
    # Initialize M
    M = 0
    for h, s in HS:
        M = max(M, h + s * N)

    left, right = 0, M
    while right - left > 1:
        mid = (left + right) // 2
        
        ok = True
        t = [0] * N
        for i in range(N):
            h, s = HS[i]
            if mid < h:
                ok = False
            else:
                t[i] = (mid - h) // s
        
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
