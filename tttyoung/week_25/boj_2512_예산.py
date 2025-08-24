n = int(input())
budget_list = list(map(int, input().split()))
total_budget = int(input())
result_list = [] 
start = 0 #min으로 하려다 10 10 10 / 20과 같이 같은수가 들어오는 경우에는 start과 end가 고정되어 변하지 않고 while문이 종료되어 result_list에 아무것도 없이 error발생
end = max(budget_list)

while start <= end: 
    mid = (start + end) // 2
    cal_list = [mid if mid<i else i for i in budget_list] #예산 사용 리스트
    if sum(cal_list) < total_budget: #합이 total_budget보다 작으면 start를 mid+1로 옮겨 다시 이분탐색 시작
        start = mid + 1
    else: 
        end = mid - 1
    result_list.append((sum(cal_list), mid)) #합과 mid를 튜플로 묶어서 저장

print(max(x for x in result_list if x[0] <= total_budget)[1]) #total_budget을 넘지 않는 최대합의 mid를 출력

