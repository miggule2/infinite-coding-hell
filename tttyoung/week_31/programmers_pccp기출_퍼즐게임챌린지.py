def solution(diffs, times, limit):
    times.insert(0, 0) #초기값 추가
    
    def cal(level, diffs, times): #level주어졌을때 시간계산
        result = 0
        for i in range(len(diffs)):
            sub = diffs[i] - level
            if sub <= 0:
                result += times[i+1]
            else:
                result += (times[i+1] + times[i]) * sub + times[i+1]
        return result       
               
    #이분탐색 시작
    start, end = 1, max(diffs)
    while (start <= end):    
        mid = (start + end) // 2
        if cal(mid, diffs, times) <= limit: #시간이 남거나 딱 맞을 경우
            end = mid - 1 #최솟값 찾기 위해 추가탐색
        else: #시간초과되는경우
            start = mid + 1 

    return start
    

    