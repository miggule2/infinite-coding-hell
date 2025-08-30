x, y = map(int, input().split())
z = (y*100)//x
start = 1
end = 1000000000 #최대 x값을 end로 잡음
result = -1 #if문에 해당하지 않게 되면 result의 값이 변하지 않음. 변하지 않을때가 승률이 변하지 않을때이므로 -1값이 출력

while start <= end:
    mid = (start + end) // 2
    new_z = (y+mid) * 100 // (x + mid) #게임 후의 새로운 승률
    if new_z > z: 
        result = mid #result라는 새로운 변수에 저장. mid를 그대로 출력하게될 경우 조건을 만족하는 값이 아닌 검사의 마지막값을 출력함. ex)99000 0 -> 999출력.
        end = mid - 1
    else:
        start = mid + 1
    
print(result)