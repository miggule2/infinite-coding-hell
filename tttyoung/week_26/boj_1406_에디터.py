import sys
input = sys.stdin.readline
#커서를 기준으로 스택을 양쪽으로 나눔
left = list(input().rstrip())
right = []
m = int(input())
c = len(left)
for i in range(m):
    cmd = list(input().split())
    if cmd[0] == 'L':
        if left: #left가 비어있으면 무시
            right.append(left.pop()) #커서를 왼쪽으로 옮기면서 커서 우측에 있는 문자는 right에 append
    elif cmd[0] == 'D':
        if right: #right가 비어있으면 무시
            left.append(right.pop()) #커서를 오른쪽으로 옮기면서 커서 좌측에 있는 문자는 left에 append
    elif cmd[0] == 'B':
        if left:        
            left.pop()
    else:
        left.append(cmd[1])

left.extend(reversed(right)) #뒤집어서 이어붙임
print(''.join(left))
