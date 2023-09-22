def make_753(number, N):
    cnt = 0
    if N < int(number):
        return cnt
    
    if all(i in number for i in ['7', '5', '3']):
        #print(number)
        cnt += 1
    
    for i in ['7', '5', '3']:
        cnt += make_753(number+i, N)
    return cnt

if __name__ == '__main__':
    N = int(input())
    print(make_753('0', N))
