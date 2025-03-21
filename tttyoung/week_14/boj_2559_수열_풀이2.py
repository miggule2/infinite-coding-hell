def con_temp(templist, k):
    maxtemplist = []
    hap = 0
    start = 0 
    end = 0

    while end < len(templist):
        hap += templist[end]  # end 위치 값 추가

        if end - start + 1 == k: # 리스트 크기가 k가 되면 처리 시작
            maxtemplist.append(hap)  # 최댓값 추가
            hap -= templist[start]  # 맨 앞 값 제거
            start += 1  # start 이동      
        end += 1  # end 이동

    return max(maxtemplist)  # 최댓값 반환


n, k = map(int, input().split())
templist = list(map(int, input().split()))
print(con_temp(templist, k))
        