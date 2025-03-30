def sugar(n):
    k3 = k5 = 0
    while(3*k3 + 5*k5 <= n):
        if (n - 3*k3) % 5 == 0: #3만큼 채우다가 남은게 5로 나눠떨어지면 k5의 값이 제일 클때이므로 봉지수는 최소가됨.
            k5 = (n-3*k3) // 5
            return k3 + k5
        k3 += 1 #if문을 통과하지 않으면 k3+1
    if n%3 == 0: #만약 5로 나눠떨어지지 않고 3으로만 나눠떨어질때 
        return k3-1 
    else: #아예 나눠떨어지지 않을때
        return -1

n = int(input())
print(sugar(n))

'''
N = int(input())
cnt = 0

while N >= 0:
    #5로 나누어 떨어질 때 break
    if N % 5 == 0:
        cnt += N // 5
        print(cnt)
        break
    
    #3kg 봉투 한 개씩 빼기
    N -= 3
    cnt += 1

#루프가 '자연적'으로 끝나는 경우 실행
else:
    print(-1)
'''
