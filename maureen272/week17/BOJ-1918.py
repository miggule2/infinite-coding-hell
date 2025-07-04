# BOJ - 1918 - 후위 표기식
infix = input()
stack = []
result = ''

# 연산자 우선순위
priority = {'+': 1, '-': 1, '*': 2, '/': 2}

for ch in infix:
    if ch.isalpha():  # 피연산자는 바로 출력
        result += ch
    elif ch == '(':  # 여는 괄호는 스택에 넣음
        stack.append(ch)
    elif ch == ')':  # 닫는 괄호가 나오면 '('까지 pop
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.pop()  # '(' 제거
    else:  # 연산자일 경우
        while stack and stack[-1] != '(' and priority.get(stack[-1], 0) >= priority[ch]: # 스택의 우선순위가 높거나 같으면 pop
            result += stack.pop()  # 우선순위가 높은 연산자를 결과에 추가
        stack.append(ch) # 현재 연산자를 스택에 추가

# 스택에 남아 있는 연산자 출력
while stack:
    result += stack.pop()

print(result)
