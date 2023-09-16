"""
1. eval
2. どこに＋を入れるかと，bit探索で実装できること思いつくこと．
"""


import itertools

def calc_sum(S):
    n = len(S)
    summ = 0
    
    # 間に入れるか入れないかを判断するための， bit列
    for bit_seq in itertools.product([0,1], repeat=n-1):
        formula = f'{S[0]}'
        for i, bit in enumerate(bit_seq, start=1):  # len(bit_seq) == n - 1
            if bit == 1:
                formula += '+'
            formula += S[i]
        print(f'bit : {bit_seq}')
        print(f'formula : {formula}')
        summ += eval(formula)
    
    return summ
    


if __name__ == '__main__':
    S = input()
    summ = calc_sum(S)
    print(summ)
    
    