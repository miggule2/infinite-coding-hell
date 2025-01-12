from collections import deque
N = int(input())
b_list = deque(list(map(int, input().split())))
bcopy_list = b_list #초기 위치값 저장
turn_list = []
print(bcopy_list)

while any(_ != 0 for _ in b_list): #b_list에 0이 아닌 숫자가 있는동안 while문 반복
    turn_list.append(bcopy_list.index(turn_list[0])+1) #리스트에 위치값 저장 but실패, 실패 이유는 모르겠으나 어차피 이대로 실행한다면 풍선안에 들어있는 숫자가 중복으로 나오면 정확한 index를 찾을 수 없음
    b_list[0] = 0
    b_list.rotate((-1)*bcopy_list[turn_list[-1] - 1])

print(turn_list)
