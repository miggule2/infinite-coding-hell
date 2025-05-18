def con_temp(templist, k):
    maxtemplist = []
    hap = 0
    start = 0 
    end = k-1
    hap = sum(templist[:k]) #첫번째 구간 합 구하기

    while(end < len(templist)):
        maxtemplist.append(hap) 
        hap -= templist[start]
        start += 1
        end += 1
        if end < len(templist): #if문이 없이 바로 더해준다면 앞에 있는 end+1을 했을때 리스트 범위를 벗어나도 while을 탈출하지 않고 계속 돌고있기 때문에 templist[end]를 더하려고 하면서 list범위를 벗어남.
            hap += templist[end]   
    return max(maxtemplist)

n, k = map(int, input().split())
templist = list(map(int, input().split()))
print(con_temp(templist, k))
        