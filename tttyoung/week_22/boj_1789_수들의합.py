s = int(input())
num = 0
i = 0 #더해주는 숫자
count = 0 #숫자 개수

#while문 반복동안 num, i, count늘려가며 최대숫자 찾기
while True:
    if num > s: #num>s이면 이보다 한개 적은 숫자가 최대개수가 됨
        print(count-1) #count-1이 최대 개수
        break
        
    else: #숫자 늘려주는 작업
        i+=1
        count+=1
        num += i