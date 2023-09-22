import numpy as np


if __name__ == '__main__':
    N = int(input())
    A = np.array(list(map(int, input().split())))
    count = 0
    flag = 1
    
    while (1):
        for a in A:
            if a%2 != 0:
                flag = 0
                break
        if flag == 0:
            break
        A = A / 2
        #print(A)
        count += 1
        
    print(count)