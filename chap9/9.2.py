eq = '1 2 + 3 4 + *'
op = ['*', '+', '-', '/']
stack = []

for ele in eq.split():
    if ele not in op:
        stack.append(ele)
    else:
        tail = stack.pop()
        head = stack.pop()
        stack.append(eval(f'{head} {ele} {tail}'))
print(stack.pop())