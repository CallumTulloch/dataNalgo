"""
"""

def tribo(n):
    if n == 0:
        return 0    
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return tribo(n-1) + tribo(n-2) + tribo(n-3)
    
if __name__ == '__main__':
    result = tribo(30)
    print(result)
    