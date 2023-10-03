brackets = '(()()(()()))'
#brackets = '(()()(()()))('

stack = []
if brackets[0] == ')':
    exit(1)

combinations = []
for i, bracket in enumerate(brackets):
    if bracket == '(':
        stack.append(i)
    elif bracket == ')':
        try:
            idx = stack.pop()
            combinations.append([idx, i])
        except:
            exit(1)

if stack == []:
    print(combinations)