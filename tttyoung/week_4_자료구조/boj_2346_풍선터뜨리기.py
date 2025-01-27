from collections import deque
N = int(input())
b_list = deque(list(enumerate(map(int, input().split()), start = 1))) #풍선 값과 index값을 튜플로 묶어서 리스트화 시킴 start = 1은 index를 1부터 시작한다는 의미
turn_list = []

while b_list:
    idx, num = b_list[0] 
    turn_list.append(idx)
    b_list.popleft()
    if num > 0:
        b_list.rotate(1-num)
    else:
        b_list.rotate(-num)
print(' '.join(map(str, turn_list)))