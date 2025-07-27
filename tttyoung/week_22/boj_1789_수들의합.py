s = int(input())
num = 0
i = 0
count = 0

while True:
    if num > s:
        print(count-1) #count-1이 최대 개수
        break
        
    else: #숫자 늘려주는 작업
        i+=1
        count+=1
        num += i