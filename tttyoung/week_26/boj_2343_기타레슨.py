n, m = map(int, input().split())
lecture = list(map(int, input().split()))

start = max(lecture) #최대값 하나는 들어가야함
end = sum(lecture)

while start <= end:
    hap = 0
    blueray = 1 #사용한 블루레이 개수
    mid = (start+end) // 2
    for i in lecture: 
        if hap+i<=mid: #mid값을 넘기기전까지만 합치기
            hap += i
        else: 
            blueray += 1 #mid넘어가면 블루레이 한장 더 씀
            hap = i
            if blueray > m: # m을 넘기면 무조건 break 
                break
    
    if blueray <= m: #개수 충족못시키면 end를 mid-1로 전환후 다시 시행
        end = mid - 1
    else:
        start = mid + 1

print(start)
