n, s = map(int, input().split())
numlist = list(map(int, input().split()[:n]))

def find_hap(numlist, s):
    start = end = 0
    hap = numlist[start]
    lenlist = []
    while start<len(numlist) and end<len(numlist):
        if hap < s:
            end += 1
            if end == len(numlist): #합이 s보다 작으면서 end값이 마지막이면 start를 옮겨줘도 값은 더 작아지기 때문에 그 뒤의 추가적인 연산은 불필요함.
                break
            hap += numlist[end]
            
        elif hap >= s:
            count = end - start + 1
            lenlist.append(count)
            hap -= numlist[start]
            start += 1
    
    if lenlist == []:
        return 0
    else:
        return min(lenlist)

print(find_hap(numlist, s))

#입력이 5 5 / 10 1 2 2 4 일때 처음에 10이 저장된 후에 hap이 0이 되는게 좀 이상함. 문제 상황에서는 어차피 1개짜리가 제일 작을테니깐 결과값에는 영향이 없지만 hap이 10을 그대로 유지한 후에 start가 1 end가 0이 될텐데...이러면 다음 숫자가 또 15같이 큰 값이 나오면 elif로 빠질텐데 그때 count값이 0이 나옴. 10 15 23 2 3 이러면 처음 10일대 count1 그다음 15일때...count0....내가 투포인터 작동을 잘못 이해하는건지 코드가 좀 이상한건지를 모르겠음. 해결됨.
#10 15 23 2 3 입력인 경우 10이 처음에 들어가면 start:1 end:0 이 되는데 이때 hap은 0이 됨. 그러므로 자연스럽게 hap<s를 만족하여 end+=1로 start, end:1이 되고 hap은 그 다음숫자인 15가 됨.